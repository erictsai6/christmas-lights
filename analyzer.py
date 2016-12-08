

# from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
from pydub import AudioSegment


def plotSpectru(y,Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
    
    print Y
    print len(Y)
    # plot(frq,abs(Y),'r') # plotting the spectrum
    # xlabel('Freq (Hz)')
    # ylabel('|Y(freq)|')

def show_info(aname, a):
    print "Array", aname
    print "shape:", a.shape
    print "dtype:", a.dtype
    print "min, max:", a.min(), a.max()
    print

def main():
    print 'analyzer start'
    filename = 'abc.mp3'

    sound = AudioSegment.from_mp3(filename)
    sound.export('abc.wav', format='wav')

    Fs = 44100;  # sampling rate

    rate,data=read('abc.wav')
    y=data[:,1]
    lungime=len(y)
    timp=len(y)/44100.
    t=linspace(0,timp,len(y))
    
    print rate

    print data
    print len(data)

    plotSpectru(y, Fs)
    # subplot(2,1,1)
    # plot(t,y)
    # xlabel('Time')
    # ylabel('Amplitude')
    # subplot(2,1,2)
    # plotSpectru(y,Fs)
    # show()


if __name__ == '__main__':
    main()