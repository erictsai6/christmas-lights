from pydub import AudioSegment
import re

def convert_mp3_to_wav(filename):
    if filename is None:
        return
    
    wav_filename = re.sub(r'\.mp3$', '.wav', filename)

    sound = AudioSegment.from_mp3(filename)    
    sound.set_channels(1)
    sound.export(wav_filename, format='wav')

    return wav_filename

