
import time
import threading

class QueueSubscribeWorker(threading.Thread):
    def __init__(self, x, redis_queue):
        self.__x = x
        self.redis_queue = redis_queue
        self.kill_received = False
        threading.Thread.__init__(self)

    def run(self):

        while not self.kill_received:
            msg = self.redis_queue.poll()
            if msg is not None:
                
                # Process the analyzer here 
                print msg

            time.sleep(5000)
    

