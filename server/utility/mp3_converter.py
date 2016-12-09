from pydub import AudioSegment
import re
import os 

def convert_mp3_to_wav(full_filepath):
    if full_filepath is None:
        return
    
    full_wav_filepath = re.sub(r'\.mp3$', '.wav', full_filepath)

    sound = AudioSegment.from_mp3(full_filepath)    
    sound.set_channels(1)
    sound.export(full_wav_filepath, format='wav')

    return full_wav_filepath

