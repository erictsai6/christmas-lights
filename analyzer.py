

# from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft, fftpack
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
from pydub import AudioSegment

from server.utility.analyzer import fft_analyze 

def plotSpectru(y, Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    print k
    frq = k/T # two sides frequency range
    print frq    
    frq = frq[range(n/2)] # one side frequency range
    print frq

    Y = fft(y) # fft computing and normalization
    # Y = Y[range(n/2)]
    
    print Y
    print len(Y)
    print abs(Y)
    # plot(frq,abs(Y),'r') # plotting the spectrum
    # xlabel('Freq (Hz)')
    # ylabel('|Y(freq)|')

def show_info(aname, a):
    print "Array", aname
    print "shape:", a.shape
    print "dtype:", a.dtype
    print "min, max:", a.min(), a.max()    

def main():
    print 'analyzer start'
    filename = 'abc.mp3'

    sound = AudioSegment.from_mp3(filename)
    sound.set_channels(1)
    sound.export('abc.wav', format='wav')

    Fs = 44100;  # sampling rate

    rate, data = read('abc.wav')
    data = data[:,1]
    ffts = fft_analyze(data, rate)

    print len(ffts)
    print len(ffts[0])
    print ffts[0]
    


    # show_info('data', data)

    # dd = 
    # y=data[:,1]
    # show_info('y', y)

    # lungime=len(y)
    # timp=len(y)/44100.
    # t=linspace(0,timp,len(y))
    
    # print 'rate: ', rate
    # print 'data: ', data

    # print 'song length: ', len(data)/rate, 'seconds'
    # print len(data)

    # # plotSpectru(y, Fs)

    # print ''
    # print 'More analysis on different signal'

    # # Number of samplepoints
    # N = 600
    # # sample spacing
    # T = 1.0 / 800.0
    # x = linspace(0.0, N*T, N)
    # y = sin(50.0 * 2.0*pi*x) + 0.5*sin(80.0 * 2.0*pi*x)
    # yf = fft(y)
    # xf = linspace(0.0, 1.0/(2.0*T), N/2)
    # print 'x length: ', len(x)
    # print 'y length: ', len(y)

    # print 'xf length: ', len(xf)
    # print xf[0: 50]
    # print 'yf length: ', len(yf)
    # yf2 = abs(yf[:N//2])

    # print 'yf2 length: ', len(yf2)

    # for i in range(0, len(xf)):
    #     print xf[i], 'Hz', yf2[i], 'amp'

    

    # subplot(2,1,1)
    # plot(t,y)
    # xlabel('Time')
    # ylabel('Amplitude')
    # subplot(2,1,2)
    # plotSpectru(y,Fs)
    # show()


if __name__ == '__main__':
    main()