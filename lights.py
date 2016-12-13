import pygame
import time
# from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft, fftpack
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
from pydub import AudioSegment
from server.worker.light_controller import LightWorker
from server.utility.analyzer import fft_analyze

def main():
    print 'analyzer start'
    filename = 'My Shot.mp3'

    sound = AudioSegment.from_mp3(filename)
    sound.set_channels(1)
    sound.export('abc.wav', format='wav')

    Fs = 44100;  # sampling rate

    rate, data = read('abc.wav')
    data = data[:,1]
    ffts = fft_analyze(data, rate)
    pygame.mixer.init()
    pygame.mixer.music.load('abc.wav')

    light_worker = LightWorker('worker 1', ffts)
    light_worker.daemon = True
    light_worker.start()
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)


if __name__ == '__main__':
    main()

