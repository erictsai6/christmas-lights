from scipy import fft, arange, ifft
from numpy import sin, linspace, pi, array_split
from scipy.io.wavfile import read, write

def fft_analyze(data, sample_rate):
    
    # Break into subarrays of 500 ms each
    subarrays = array_split(data, sample_rate / 2)

    ffts = []
    number_of_blocks = 32

    # with a 22050 Hz band and a 32 FFT size this band gets broken down into 16 bins
    for i in range(0, len(subarrays)):
        subarray = subarrays[i]

        # n = len(subarray) # number of data points
        # k = arange(n)     # 
        # T = n / Fs        # The time in seconds
        # frq = k / T        

        fft_subarray = abs(fft(subarray, number_of_blocks)[: 32 / 2])
        ffts.append(fft_subarray)

    # TODO - not really relevant but i just wanted to keep this here for my benefit
    x_frequencies = linspace(0, sample_rate / 2, number_of_blocks)

    # Returns array of FFTs where each tick represents 500 ms
    return ffts
