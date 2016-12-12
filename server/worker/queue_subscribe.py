import time
import threading
import pygame

class QueueSubscribeWorker(threading.Thread):
    def __init__(self, x, redis_queue):
        self.__x = x
        self.redis_queue = redis_queue
        self.kill_received = False
        threading.Thread.__init__(self)

    def run(self):

        while not self.kill_received:
            try:
                msg = self.redis_queue.poll()

                if msg is not None:
                    
                    # Process the analyzer here 
                    print msg

                    pygame.mixer.init()
                    pygame.mixer.music.load(msg['filepath'])
                    pygame.mixer.music.play()

                    # Blocks music playback 
                    while pygame.mixer.music.get_busy(): 
                        pygame.time.Clock().tick(10)

                time.sleep(5)
            except Exception, e:
                print 'Failed to poll message', e
    

