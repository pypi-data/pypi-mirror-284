import functools
import logging
import re
import io
import serial
import string
import time
import asyncio
import threading
import binascii
import codecs
from functools import wraps
from typing import Callable, Coroutine
from threading import RLock

_LOGGER = logging.getLogger(__name__)
# #T'B'ON,FM89.1
TUNER_STATUS_PATTERN = re.compile('T\'(?P<tuner>|A|B)\''
                     '(?P<power>ON|OFF),'
                     '(?P<band>|AM|FM|SR|DAB)'
                     '(?P<freq>[0-9.]+)')
# #T’x’BANDSa[,b][,c]
TUNER_BANDS_PATTERN = re.compile(r'T\\\'(?P<tuner>A|B).+'
                     'BANDS\"(?P<bands>.+)\'')
# #T'A'ARTIST"Artist"
TUNER_ARTIST_PATTERN = re.compile(r'T\\\'(?P<tuner>A|B).+'
                     'ARTIST\"(?P<artist>.+|\")\'')
# #T'A'TITLE"Title"
TUNER_TITLE_PATTERN = re.compile(r'T\\\'(?P<tuner>A|B).+'
                     'TITLE\"(?P<title>.+|\")\'')
# #T'A'CHAN"Channel"
TUNER_CHAN_PATTERN = re.compile(r'T\\\'(?P<tuner>A|B).+'
                     'CHAN\"(?P<channel>.+|\")\'')
# #T'A'PRESET101,"DESC"
TUNER_PRESET_PATTERN = re.compile(r'T\\\'(?P<tuner>A|B).+'
                     'PRESET(?P<preset>[0-9.]+),\"(?P<desc>.+|\")\'')
# #VER"NV-T2SIR FWv1.18 HWv40
T2SIR_VERSION = re.compile('VER\"NV-T2SIR[A-Za-z\t .]+')

# #OFF
OFF_PATTERN = re.compile('OFF')

T2SIR_CFG1_PATTERN = re.compile('T2SIR-CONFIG')

# #T'A'_LISTSR184,0,"Sirius Preview"
SRLIST_PATTERN = re.compile(r'T\\\'(?P<tuner>A|B).+'
                 '_LISTSR(?P<freq>[0-9.]+),.+,(?P<channel>.+)\'')

# #?
ERROR_PATTERN = re.compile('\?')

EOL = b'\r'
TIMEOUT_RESPONSE = 0.1     # Number of seconds before command response timeout
tuner_a_artist = ''
tuner_b_artist = ''
tuner_a_title = ''
tuner_b_title = ''
tuner_a_channel = ''
tuner_b_channel = ''
tuner_a_source_ch = []
tuner_b_source_ch = []
tuner_a_source_list = []
tuner_b_source_list = []
tuner_a_source_list.append(' ')
tuner_b_source_list.append(' ')
tuner_a_bands = []
tuner_b_bands = []
tuner_a_preset_ch = []
tuner_b_preset_ch = []
tuner_a_preset_list = []
tuner_b_preset_list = []
tuner_a_sr_chlist_setup = 0
tuner_b_sr_chlist_setup = 0
tuner_a_sr_chlist = []
tuner_b_sr_chlist = []
tuner_a_sr_name = []
tuner_b_sr_name = []
preset_bankname = []
preset_bank = []
preset_band = []
preset_num = []
preset_name = []
preset_fav = []
media_tunertable = []
media_callback = []
tunerpwr = False
tuner_a_init = 0
tuner_b_init = 0
tuner_a_freq = 0
tuner_b_freq = 0
tuner_a_band = 'UNK'
tuner_b_band = 'UNK'
read_config = False

class TunerStatus(object):
    def __init__(self
                 ,tuner: str
                 ,power: bool
                 ,band: str
                 ,freq: str
                 ,from_port: bool
                 ):
        global tunerpwr
        global tunerpwrontime
        global tuner_a_band
        global tuner_a_freq
        global tuner_a_channel
        global tuner_a_artist
        global tuner_a_title
        global tuner_a_source_list
        global tuner_b_band
        global tuner_b_freq
        global tuner_b_channel
        global tuner_b_artist
        global tuner_b_title
        global tuner_b_source_list
        self.tuner = tuner

        if self.tuner == 'A':
            if from_port:
                tuner_a_band = band
                tuner_a_freq = freq
            self.band = tuner_a_band
            self.freq = tuner_a_freq
            self.channel = tuner_a_channel
            self.artist = tuner_a_artist
            self.title = tuner_a_title
            self.sources = tuner_a_source_list

        if self.tuner == 'B':
            if from_port:
                tuner_b_band = band
                tuner_b_freq = freq
            self.band = tuner_b_band
            self.freq = tuner_b_freq
            self.channel = tuner_b_channel
            self.artist = tuner_b_artist
            self.title = tuner_b_title
            self.sources = tuner_b_source_list

        if power:
           if tunerpwr == False:
               tunerpwrontime = time.time()
           tunerpwr = True
        else:
           tunerpwr = False

        self.power = tunerpwr

        if from_port:
            if self.tuner in media_tunertable:
                callbackobj = media_tunertable.index(self.tuner)
                callbackint = int(callbackobj)
                media_callback[callbackint]()

        _LOGGER.debug('Tuner %s: Power: %s | Band: %s | Freq: %s | Channel: %s | Artist: %s | Title: %s', \
           self.tuner, self.power, self.band, self.freq, self.channel, self.artist, self.title)

    @classmethod
    def from_string(cls, match):
        TunerStatus(*[str(m) for m in match.groups()], True)

class TunerChannel(object):
    def __init__(self
                 ,tuner: str
                 ,channel: str
                 ):
        channel = codecs.decode(channel, 'unicode_escape')
        channel = channel.replace('"', '')
        channel = channel.replace('\\', '')
        global tuner_a_channel
        global tuner_b_channel
        if tuner == 'A':
            tuner_a_channel = channel
        if tuner == 'B':
            tuner_b_channel = channel

        if tuner in media_tunertable:
            callbackobj = media_tunertable.index(tuner)
            callbackint = int(callbackobj)
            media_callback[callbackint]()

    @classmethod
    def from_string(cls, match):
        TunerChannel(*[str(m) for m in match.groups()])

class TunerPreset(object):
    def __init__(self
                 ,tuner: str
                 ,preset: str
                 ,desc: str
                 ):

        # For possible future use
        pass

    @classmethod
    def from_string(cls, match):
        TunerPreset(*[str(m) for m in match.groups()])

class TunerArtist(object):
    def __init__(self
                 ,tuner: str
                 ,artist: str
                 ):
        artist = codecs.decode(artist, 'unicode_escape')
        artist = artist.replace('"', '')
        artist = artist.replace('\\', '')
        global tuner_a_artist
        global tuner_b_artist
        if tuner == 'A':
            tuner_a_artist = artist
        if tuner == 'B':
            tuner_b_artist = artist

    @classmethod
    def from_string(cls, match):
        TunerArtist(*[str(m) for m in match.groups()])

class TunerTitle(object):
    def __init__(self
                 ,tuner: str
                 ,title: str
                 ):
        title = codecs.decode(title, 'unicode_escape')
        title = title.replace('"', '')
        title = title.replace('\\', '')
        global tuner_a_title
        global tuner_b_title
        if tuner == 'A':
            tuner_a_title = title
        if tuner == 'B':
            tuner_b_title = title

        if tuner in media_tunertable:
            callbackobj = media_tunertable.index(tuner)
            callbackint = int(callbackobj)
            media_callback[callbackint]()

    @classmethod
    def from_string(cls, match):
        TunerTitle(*[str(m) for m in match.groups()])

class TunerBands(object):
    def __init__(self
                 ,tuner: str
                 ,bands: str
                 ):
        global tuner_a_bands
        global tuner_b_bands
        bands = bands.replace('"', '')
        _LOGGER.debug('Tuner %s supports bands %s', tuner, bands.split(','))
        if tuner == 'A':
            if tuner_a_bands != bands:
                tuner_a_bands = bands
                _LOGGER.debug('Tuner %s bands added/removed', tuner)
                PresetLists()
        if tuner == 'B':
            if tuner_b_bands != bands:
                tuner_b_bands = bands
                _LOGGER.debug('Tuner %s bands added/removed', tuner)
                PresetLists()

    @classmethod
    def from_string(cls, match):
        TunerBands(*[str(m) for m in match.groups()])

class T2SIRConfig(object):
    def __init__(self
                 ):
        global config_data_1
        global config_data_2
        global preset_bankname
        global preset_bank
        global preset_band
        global preset_num
        global preset_name
        global preset_fav
        preset_bankname = []
        preset_bank = []
        preset_band = []
        preset_num = []
        preset_name = []
        preset_fav = []

        _LOGGER.debug('Config data [1/2]: %s', config_data_1)
        _LOGGER.debug('Config data [2/2]: %s', config_data_2)
        config_data_1 = binascii.hexlify(config_data_1)
        config_data_2 = binascii.hexlify(config_data_2)
        config_data_1 = config_data_1.replace(b'\n', b'\x00')
        config_data_2 = config_data_2.replace(b'\n', b'\x00')

        # Process bank names in part 1 config data
        bnkstart = 2126
        bnknum = 1
        while bnknum < 6:
            bnkend = bnkstart + 40
            self.proc_t2sir_bank_data(bnknum, config_data_1[bnkstart:bnkend])
            bnkstart = bnkstart + 132
            bnknum += 1

        # Process presets in part 2 config data
        pstread = 0
        pststart = 0
        pstbank = 1
        pstnum = 1
        while pstbank < 6 and pstnum < 21:
            pstend = pststart + 129
            self.proc_t2sir_preset_data(pstbank, pstnum, config_data_2[pststart:pstend])
            pstread = pstread + 132
            if pstread%1056 == 0:
                pststart = pststart + 4
            pststart = pststart + 132
            pstnum += 1
            if pstnum == 21:
                pstbank += 1
                pstnum = 1

        PresetLists()

    @classmethod
    def proc_t2sir_bank_data(cls, banknum, data):
        bankname = binascii.unhexlify(data)
        bankname = bankname.replace(b'\x0b', b'1')
        bankname = bankname.replace(b'\x00', b'')
        bankname = codecs.decode(bankname, 'unicode-escape')
        preset_bankname.append(bankname)
        _LOGGER.debug('Bank %s - %s', banknum, bankname)

    @classmethod
    def proc_t2sir_preset_data(cls, pstbank, pstnum, data):
        fav = data[127:128]
        fav = True if fav == b'1' else False
        name = data[18:120]
        band = data[9:10]
        if band == b'0':
            band = None
        elif band == b'1':
            band = 'SR'
        elif band == b'2':
            band = 'FM'
        elif band == b'3':
            band = 'AM'
        else:
            band = 'UNK'
        name = binascii.unhexlify(name)
        name = name.replace(b'\x0b', b'1')
        name = name.replace(b'\x00', b'')
        name = codecs.decode(name, 'unicode_escape')
        if name != '':
            _LOGGER.debug('Bank %s, Preset %s | Band: %s | Name: %s | Fav: %s', \
                pstbank, pstnum, band, name, fav)
            preset_bank.append(pstbank)
            preset_band.append(band)
            preset_num.append(pstnum)
            preset_name.append(name)
            preset_fav.append(fav)
        return

class SiriusChannel(object):
    def __init__(self
                 ,tuner: str
                 ,freq: str
                 ,channel: str
                 ):
        global tuner_a_sr_chlist
        global tuner_a_sr_name
        global tuner_b_sr_chlist
        global tuner_b_sr_name
        channel = codecs.decode(channel, 'unicode_escape')
        channel = channel.replace('"', '')
        channel = channel.replace('\\', '')
        _LOGGER.debug('Tuner %s received SiriusXM ch %s - %s', tuner, freq, channel)

        if freq == '0':
            # Start of new channel lineup, remove current if exists
            _LOGGER.debug('Ignoring ID channel.')
            if tuner == 'A':
                tuner_a_sr_chlist = []
                tuner_a_sr_name = []
            elif tuner == 'B':
                tuner_b_sr_chlist = []
                tuner_b_sr_name = []
        elif re.search('Preview', channel):
            _LOGGER.debug('Ignoring Preview channel.')
        elif tuner == 'A':
            tuner_a_sr_chlist.append(freq)
            tuner_a_sr_name.append(channel)
            SourceLists()
        elif tuner == 'B':
            tuner_b_sr_chlist.append(freq)
            tuner_b_sr_name.append(channel)
            SourceLists()

    @classmethod
    def from_string(cls, match):
        SiriusChannel(*[str(m) for m in match.groups()])

class SourceLists(object):
    def __init__(self):
        # Build "source list" from presets and Sirius channels if either avail
        global tuner_a_source_list
        global tuner_a_source_ch
        global tuner_b_source_list
        global tuner_b_source_ch
        tuner_a_source_ch = []
        tuner_b_source_ch = []
        tuner_a_source_list = []
        tuner_b_source_list = []
        for pst in range(len(tuner_a_preset_list)):
            preset_ch = 'PRESET' + str(tuner_a_preset_ch[pst])
            tuner_a_source_ch.append(preset_ch)
            tuner_a_source_list.append(tuner_a_preset_list[pst])
        for pst in range(len(tuner_b_preset_list)):
            preset_ch = 'PRESET' + str(tuner_b_preset_ch[pst])
            tuner_b_source_ch.append(preset_ch)
            tuner_b_source_list.append(tuner_b_preset_list[pst])
        if 'SR' in tuner_a_bands:
            for ch in range(len(tuner_a_sr_chlist)):
                sr_ch = 'SR' + str(tuner_a_sr_chlist[ch])
                tuner_a_source_ch.append(sr_ch)
                sr_chname = 'SR ' + tuner_a_sr_chlist[ch] + ' - ' + tuner_a_sr_name[ch]
                tuner_a_source_list.append(sr_chname)
        if 'SR' in tuner_b_bands:
            for ch in range(len(tuner_b_sr_chlist)):
                sr_ch = 'SR' + str(tuner_b_sr_chlist[ch])
                tuner_b_source_ch.append(sr_ch)
                sr_chname = 'SR ' + tuner_b_sr_chlist[ch] + ' - ' + tuner_b_sr_name[ch]
                tuner_b_source_list.append(sr_chname)
        if len(tuner_a_source_list) == 0:
            _LOGGER.debug('Source list A empty')
            tuner_a_source_list.append(' ')
        if len(tuner_b_source_list) == 0:
            _LOGGER.debug('Source list B empty')
            tuner_b_source_list.append(' ')
        if 'A' in media_tunertable:
            callbackobj = media_tunertable.index('A')
            callbackint = int(callbackobj)
            media_callback[callbackint]()
        if 'B' in media_tunertable:
            callbackobj = media_tunertable.index('B')
            callbackint = int(callbackobj)
            media_callback[callbackint]()

class PresetLists(object):
    def __init__(self):
        # Process presets, favorites, and sat channels into a list
        global tuner_a_preset_ch
        global tuner_a_preset_list
        global tuner_b_preset_ch
        global tuner_b_preset_list
        tuner_a_preset_ch = []
        tuner_a_preset_list = []
        tuner_b_preset_ch = []
        tuner_b_preset_list = []
        for pst in range(len(preset_fav)):
            if preset_fav[pst] == True:
                bank = preset_bank[pst]
                bank -= 1
                fav = preset_bankname[bank] + ': ' + str(preset_num[pst]) + \
                      ' - ' + preset_name[pst]
                if preset_band[pst] in tuner_a_bands:
                     tuner_a_preset_ch.append(str(bank + 1) + str(preset_num[pst]))
                     tuner_a_preset_list.append(fav)
                     _LOGGER.debug('Added tuner A fav: %s', fav)
                if preset_band[pst] in tuner_b_bands:
                     tuner_b_preset_ch.append(str(bank + 1) + str(preset_num[pst]))
                     tuner_b_preset_list.append(fav)
                     _LOGGER.debug('Added tuner B fav: %s', fav)
        for pst in range(len(preset_fav)):
            if preset_fav[pst] != True:
                bank = preset_bank[pst]
                bank -= 1
                preset = preset_bankname[bank] + ': ' + str(preset_num[pst]) + \
                         ' - ' + preset_name[pst]
                if preset_band[pst] in tuner_a_bands:
                     tuner_a_preset_ch.append(str(bank + 1) + str(preset_num[pst]))
                     tuner_a_preset_list.append(preset)
                     _LOGGER.debug('Added tuner A preset: %s', preset)
                if preset_band[pst] in tuner_b_bands:
                     tuner_b_preset_ch.append(str(bank + 1) + str(preset_num[pst]))
                     tuner_b_preset_list.append(preset)
                     _LOGGER.debug('Added tuner B preset: %s', preset)
        SourceLists()

class Nuvo(object):
    """
    Nuvo tuner interface
    """
    def add_callback(self, coro: Callable[..., Coroutine], tuner, tuner_name) -> None:
        """
        Add entity subscription for updates
        """
        raise NotImplemented()

    def get_model(self):
        """
        Get the Nuvo model from version request
        """
        raise NotImplemented()

    def tuner_status(self, tuner: str):
        """
        Get the structure representing the status of the tuner
        :param tuner: tuner A or B
        :return: status of the tuner or None
        """
        raise NotImplemented()

    def set_power(self, power: bool):
        """
        Turn tuner on or off
        :param power: True to turn on, False to turn off
        """
        raise NotImplemented()

    def media_previous_track(self, tuner: str):
        """
        Send channel seek/tune down or prev preset command
        """
        raise NotImplemented()

    def media_next_track(self, tuner: str):
        """
        Send channel seek/tune up or next preset command
        """
        raise NotImplemented()

    def tune(self, tuner: str, media_id: str):
        """
        Tune a channel or other uses
        """
        raise NotImplemented()

    def set_source(self, tuner: str, source: str):
        """
        Set freq/channel for tuner
        """
        raise NotImplemented()

    def set_freq(self, tuner: str, freq: str):
        """
        Set the tuner band/frequency.
        """
        raise NotImplemented()

# Helpers

def _parse_response(string: bytes):
   """
   :param request: request that is sent to the nuvo
   :return: regular expression return match(s)
   """
   global MODEL

   match = re.search(TUNER_STATUS_PATTERN, string)
   if match:
      TunerStatus.from_string(match)

   if not match:
       match = re.search(T2SIR_CFG1_PATTERN, string)
       if match:
          _LOGGER.debug('T2-SIR config received')
          T2SIRConfig()

   if not match:
       match = re.search(TUNER_PRESET_PATTERN, string)
       if match:
          _LOGGER.debug('Preset message received')
          TunerPreset.from_string(match)

   if not match:
       match = re.search(TUNER_CHAN_PATTERN, string)
       if match:
          _LOGGER.debug('Channel message received')
          TunerChannel.from_string(match)

   if not match:
       match = re.search(TUNER_ARTIST_PATTERN, string)
       if match:
          _LOGGER.debug('Artist message received')
          TunerArtist.from_string(match)

   if not match:
       match = re.search(TUNER_TITLE_PATTERN, string)
       if match:
          _LOGGER.debug('Title message received')
          TunerTitle.from_string(match)

   if not match:
       match = re.search(TUNER_BANDS_PATTERN, string)
       if match:
          TunerBands.from_string(match)

   if not match:
       match = re.search(SRLIST_PATTERN, string)
       if match:
          SiriusChannel.from_string(match)

   if not match:
       match = re.search(OFF_PATTERN, string)
       if match:
          _LOGGER.debug('Power off received')
          power_off()

   if not match:
       match = re.search(ERROR_PATTERN, string)
       if match:
          _LOGGER.error('Received error response from Nuvo on last command')

   if not match:
       match = re.search(T2SIR_VERSION, string)
       if match:
          _LOGGER.info('Nuvo returned model T2-SIR')
          MODEL = 'T2-SIR'

def _format_version_request():
    return 'VER'.format()

def _format_tuner_status_request(tuner: str) -> str:
    return "T\'{}\'STATUS".format(tuner)

def _format_tuner_channel_request(tuner: str) -> str:
    return "T\'{}\'CHAN".format(tuner)

def _format_tuner_artist_request(tuner: str) -> str:
    return "T\'{}\'ARTIST".format(tuner)

def _format_tuner_title_request(tuner: str) -> str:
    return "T\'{}\'TITLE".format(tuner)

def _format_tuner_bands_request(tuner: str) -> str:
    return "T\'{}\'BANDS".format(tuner)

def _format_tuner_config_request(tuner: str) -> str:
    global read_config
    read_config = True
    return "_CFG1".format(tuner)

def _format_sr_chlist_request(tuner: str) -> str:
    return "T\'{}\'_LISTSR".format(tuner)

def _format_tune_up(tuner: str) -> str:
    return "T\'{}\'TUNE+".format(tuner)

def _format_tune_down(tuner: str) -> str:
    return "T\'{}\'TUNE-".format(tuner)

def _format_seek_up(tuner: str) -> str:
    return "T\'{}\'SEEK+".format(tuner)

def _format_seek_down(tuner: str) -> str:
    return "T\'{}\'SEEK-".format(tuner)

def _format_next_preset(tuner: str) -> str:
    return "T\'{}\'PRESET+".format(tuner)

def _format_prev_preset(tuner: str) -> str:
    return "T\'{}\'PRESET-".format(tuner)

def _format_next_band(tuner: str) -> str:
    return "T\'{}\'SRC+".format(tuner)

def _format_am_band(tuner: str) -> str:
    return "T\'{}\'SRCAM".format(tuner)

def _format_fm_band(tuner: str) -> str:
    return "T\'{}\'SRCFM".format(tuner)

def _format_sr_band(tuner: str) -> str:
    return "T\'{}\'SRCSR".format(tuner)

def _format_tune(tuner: str, media_id: str) -> str:
    return "T\'{}\'{}".format(tuner, media_id)

def _format_set_power(power: bool) -> str:
    if (power):
       return '*ON'
    else:
       return '*OFF'

def power_off():
    global tunerpwr
    tunerpwr = False
    if 'A' in media_tunertable:
        callbackobj = media_tunertable.index('A')
        callbackint = int(callbackobj)
        media_callback[callbackint]()
    if 'B' in media_tunertable:
        callbackobj = media_tunertable.index('B')
        callbackint = int(callbackobj)
        media_callback[callbackint]()

def get_nuvo(port_url, baud, conf_track):
    """
    Return synchronous version of Nuvo interface
    :param port_url: serial port, i.e. '/dev/ttyUSB0,/dev/ttyS0'
    :param baud: baud, i.e '9600'
    :return: synchronous implementation of Nuvo interface
    """
    lock = RLock()
    global track
    track = conf_track

    def synchronized(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)
        return wrapper

    class NuvoSync(Nuvo):
        def __init__(self, port_url):
            pass

        def get_model(self):
            findmodelcount = 0
            global MODEL
            while findmodelcount < 10:
                self._process_request(_format_version_request())
                time.sleep(TIMEOUT_RESPONSE)
                if 'MODEL' in globals():
                    findmodelcount = 10
                else:
                    findmodelcount += 1
            if not 'MODEL' in globals():
                _LOGGER.error('This does not appear to be a supported Nuvo tuner, '\
                              'however setup will still continue.  Please open a '\
                              'support request on github for possible future support.')
                MODEL = 'Unknown'
            return MODEL

        def _send_request(self, request):
            #format and send output command
            lineout = "*" + request + "\r"
            _LOGGER.debug('Sending "%s"', request)
            if request == "_CFG1":
                try:
                    port.write(lineout.encode())
                    ackcount = 0
                    while ackcount < 30:
                        time.sleep(0.1)
                        lineout = "\x06"
                        port.write(lineout.encode())
                        ackcount += 1
                except:
                    _LOGGER.error('Unexpected port error when sending command.')
                    return False
            else:
                try:
                    port.write(lineout.encode())
                except:
                    _LOGGER.error('Unexpected port error when sending command.')
                    return False
            return True

        def _process_request(self, request: str):
            # Send command to device
            self._send_request(request)

        def _listen():
            timeout = TIMEOUT_RESPONSE
            _LOGGER.info('Attempting connection - "%s" at %s baud', port_url, baud)
            global listen_init
            listen_init = 1

            # listen for response
            def read_data():
                global listen_init
                global port
                global read_config
                global config_data_1
                global config_data_2
                try:
                    port = serial.serial_for_url(port_url, do_not_open=True)
                    port.baudrate = int(baud)
                    port.stopbits = serial.STOPBITS_ONE
                    port.bytesize = serial.EIGHTBITS
                    port.parity = serial.PARITY_NONE
                    port.open()
                except:
                    if listen_init == 1:
                         return False

                no_data = False
                receive_buffer = b''
                message = b''
                listen_init = 0
                try:
                    while (no_data == False):
                    # fill buffer until we get term seperator
                       data = port.read(1)
                       if data:
                           receive_buffer += data
                           if read_config:
                               if configpos == 0:
                                   receive_buffer = data
                               configpos += 1
                               if configpos == 1590:
                                   config_data_1 = receive_buffer
                                   receive_buffer = b''
                               if configpos == 8220:
                                   read_config = False
                                   config_data_2 = receive_buffer
                                   receive_buffer = b''
                                   _parse_response('T2SIR-CONFIG')
                           else:
                               configpos = 0
                               if EOL in receive_buffer:
                                   message, sep, receive_buffer = receive_buffer.partition(EOL)
                                   _LOGGER.debug('Received: %s', str(message))
                                   _parse_response(str(message))
                except:
                    _LOGGER.error('Unexpected port error, retrying.')
                    time.sleep(5)
                    try:
                        port.open()
                        read_data()
                    except:
                        read_data()

            read_data()

        SyncThread = threading.Thread(target=_listen, args=(), daemon=True)
        SyncThread.start()

        def add_callback(self, callback: Callable[..., Coroutine], tuner) -> None:
            global media_tunertable
            global media_callback
            media_tunertable.append(tuner)
            media_callback.append(callback)
            _LOGGER.debug('Added Nuvo Tuner %s callback: %s', tuner, callback)

        @synchronized
        def tuner_status(self, tuner: str):
            global tunerpwr
            global tunerpwrontime
            global tuner_a_init
            global tuner_a_sr_chlist_setup
            global tuner_b_init
            global tuner_b_sr_chlist_setup

            if tuner_a_init == 0:
                tuner_a_init += 1
                try:
                    self._process_request(_format_tuner_config_request(tuner))
                except:
                    pass

            if tuner_a_init < 2 or tuner_b_init < 2:
                try:
                    self._process_request(_format_tuner_status_request(tuner))
                    self._process_request(_format_tuner_channel_request(tuner))
                    self._process_request(_format_tuner_artist_request(tuner))
                    self._process_request(_format_tuner_title_request(tuner))
                    self._process_request(_format_tuner_bands_request(tuner))
                except:
                    pass
                if tuner == 'A':
                    tuner_a_init += 1
                if tuner == 'B':
                    tuner_b_init += 1

            # Refresh Sirius channel list every 24h and when band first avail
            time24hago = time.time() - 86400
            if 'SR' in tuner_a_bands and time24hago > tuner_a_sr_chlist_setup \
                    and tuner == 'A' and tuner_a_init == 3 and \
                    tunerpwrontime < (time.time() - 180):
                tuner_a_sr_chlist_setup = time.time()
                self._process_request(_format_sr_chlist_request(tuner))
            if 'SR' in tuner_b_bands and time24hago > tuner_a_sr_chlist_setup \
                    and tuner == 'B' and tuner_b_init == 3:
                tuner_b_sr_chlist_setup = True
                self._process_request(_format_sr_chlist_request(tuner))

            if tunerpwr == True:
                self.power = bool(1)
            else:
                self.power = bool(0)
            if tuner == 'A':
                self.band = tuner_a_band
                self.freq = tuner_a_freq
                self.channel = tuner_a_channel
                self.artist = tuner_a_artist
                self.title = tuner_a_title

            if tuner == 'B':
                self.band = tuner_b_band
                self.freq = tuner_b_freq
                self.channel = tuner_b_channel
                self.artist = tuner_b_artist
                self.title = tuner_b_title

            return TunerStatus(tuner, self.power, self.band, self.freq, False)

        @synchronized
        def set_power(self, power: bool):
            self._process_request(_format_set_power(power))

        @synchronized
        def media_previous_track(self, tuner: str):
            if track == 'tune':
                self._process_request(_format_tune_down(tuner))
            elif track == 'seek':
                self._process_request(_format_seek_down(tuner))
            elif track == 'preset':
                self._process_request(_format_prev_preset(tuner))
            else:
                _LOGGER.error('Invalid track setting.  Selecting seek for you.')
                self._process_request(_format_seek_down(tuner))

        @synchronized
        def media_next_track(self, tuner: str):
            if track == 'tune':
                self._process_request(_format_tune_up(tuner))
            elif track == 'seek':
                self._process_request(_format_seek_up(tuner))
            elif track == 'preset':
                self._process_request(_format_next_preset(tuner))
            else:
                _LOGGER.error('Invalid track setting.  Selecting seek for you.')
                self._process_request(_format_seek_up(tuner))

        @synchronized
        def tune(self, tuner: str, media_id: str):
            _LOGGER.debug('Media play "%s" for tuner %s', media_id, tuner)
            if str.upper(media_id) == 'SEEK-':
                self._process_request(_format_seek_down(tuner))
            elif str.upper(media_id) == 'SEEK+':
                self._process_request(_format_seek_up(tuner))
            elif str.upper(media_id) == 'TUNE-':
                self._process_request(_format_tune_down(tuner))
            elif str.upper(media_id) == 'TUNE+':
                self._process_request(_format_tune_up(tuner))
            elif str.upper(media_id) == 'PRESET-':
                self._process_request(_format_prev_preset(tuner))
            elif str.upper(media_id) == 'PRESET+':
                self._process_request(_format_next_preset(tuner))
            elif str.upper(media_id) == 'BAND':
                self._process_request(_format_next_band(tuner))
            elif str.upper(media_id) == 'RELOAD':
                self.reload_config(tuner)
            elif str.upper(media_id) == 'AM':
                self._process_request(_format_am_band(tuner))
            elif str.upper(media_id) == 'FM':
                self._process_request(_format_fm_band(tuner))
            elif str.upper(media_id) == 'SR':
                self._process_request(_format_sr_band(tuner))
            else:
                if re.match(r'[0-9.]+', media_id):
                    if tuner == 'A':
                        media_id = tuner_a_band + media_id
                    elif tuner == 'B':
                        media_id = tuner_b_band + media_id
                self._process_request(_format_tune(tuner, media_id))

        @synchronized
        def set_source(self, tuner: str, source: str):
            try:
                if tuner == 'A':
                    sourceindexobj = [i for i, x in enumerate(tuner_a_source_list) \
                                     if x == source]
                    sourceindex = int(sourceindexobj[0])
                    tunecmd = "T\'A\'" + tuner_a_source_ch[sourceindex]
                elif tuner == 'B':
                    sourceindexobj = [i for i, x in enumerate(tuner_b_source_list) \
                                     if x == source]
                    sourceindex = int(sourceindexobj[0])
                    tunecmd = "T\'B\'" + tuner_b_source_ch[sourceindex]
                self._send_request(tunecmd)
            except:
                _LOGGER.error('Can not process source list for tuner %s', tuner)

        @synchronized
        def reload_config(self, tuner: str):
            global tuner_a_sr_chlist_setup
            global tuner_b_sr_chlist_setup
            global tuner_a_sr_chlist
            global tuner_b_sr_chlist
            global tuner_a_sr_chname
            global tuner_b_sr_chname
            tuner_a_sr_chlist_setup = 0
            tuner_b_sr_chlist_setup = 0
            tuner_a_sr_chlist = []
            tuner_b_sr_chlist = []
            tuner_a_sr_chname = []
            tuner_b_sr_chname = []
            self._process_request(_format_tuner_config_request(tuner))
            PresetLists()
            SourceLists()

    return NuvoSync(port_url)
