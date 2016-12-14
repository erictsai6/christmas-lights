import time
import threading
import pygame
import json
from scipy.io.wavfile import read,write
from scipy import fft, arange, ifft, fftpack
from server.worker.light_controller import LightWorker
from server.utility.analyzer import fft_analyze
import RPi.GPIO as GPIO

class QueueSubscribeWorker(threading.Thread):
    def __init__(self, x, redis_queue):
        self.__x = x
        self.redis_queue = redis_queue
        self.kill_received = False
        threading.Thread.__init__(self)

    def run(self):

        while not self.kill_received:
            try:
                msg_list = self.redis_queue.get_list()

                if msg_list is not None and len(msg_list) > 0:
                    
                    msg = json.loads(msg_list[-1])
                    rate, data = read(msg['data']['filepath'])
                    data = data[:,1]
                    ffts = fft_analyze(data, rate)
                    # Process the analyzer here 
                    print msg['data']['filepath']
                    light_worker = LightWorker('worker 1', ffts)
                    light_worker.daemon = True
                    light_worker.start()
                    pygame.mixer.init()
                    pygame.mixer.music.load(msg['data']['filepath'])
                    pygame.mixer.music.play()

                    # Blocks music playback 
                    while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)

                    light_worker.kill_received = True

                    # Finally remove it from the list
                    self.redis_queue.poll()


            except Exception, e:
                print 'Failed to poll message', e 
            time.sleep(5)
        GPIO.cleanup()

