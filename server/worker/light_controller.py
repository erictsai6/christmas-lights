import time
import threading
import pygame
import json
import math
import RPi.GPIO as GPIO

class LightWorker(threading.Thread):
    def __init__(self, x, fft):
        self.__x = x
        self.kill_received = False
        self.fft = fft
        self.pinList = [2, 3, 4, 17, 27, 22, 10, 9]
        GPIO.setmode(GPIO.BCM)

        for i in self.pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        self.previousState = []
        for i in range(0, 16):
            self.previousState.append(
                {
                    'state': False,
                    'value': 0
                }
            )
        threading.Thread.__init__(self)
        # background_colour = (255,255,255)
        # (width, height) = (600, 400)

        # self.screen = pygame.display.set_mode((width, height))
        # pygame.display.set_caption('Lights Visualizer')
        # self.screen.fill(background_colour)

        # pygame.display.flip()
    
    def color(self, state):
        colors= [
            (237, 215, 247),
            (79, 158, 113),
            (214, 120, 70),
            (4, 140, 209),
            (209, 209, 4),
            (196, 5, 21),
            (5, 196, 167),
            (239, 207, 64)
        ];
        black = (0,0,0)
        width = 600/4
        height = 200
        for i in range(1, 9):
            j = i -1
            x = j%4 * width
            y = j/4 * height
            if state[j]: 
                GPIO.output(self.pinList[j], GPIO.HIGH)
                #pygame.draw.rect(self.screen, colors[j], (x,y,width,height), 0)
            else: 
                GPIO.output(self.pinList[j], GPIO.LOW)
                #pygame.draw.rect(self.screen, black, (x,y,width,height), 0)

        #pygame.display.flip()

    def getState(self, state):
        result = []
        for i in range(0, len(state)):
            result.append(self.compare(state[i], i))
        return result

    def compare(self, value, i):
        prev = self.previousState[i]
        threshhold = prev['value'] * .5
        if prev['state']:
            if value + threshhold < prev['value']:
                self.previousState[i] = {
                    'state': False,
                    'value': value
                }
                return False
            else:
                if value > prev['value']:
                    self.previousState[i] = {
                        'state': True,
                        'value': value
                    }                  
                return True
        else:
            if value - threshhold > prev['value']:
                self.previousState[i] = {
                    'state': True,
                    'value': value
                }
                return True
            else:
                if value < prev['value']:
                    self.previousState[i] = {
                        'state': False,
                        'value': value
                    }                  
                return False        


    def run(self):
        start = time.time()
        end = time.time()
        try:
            i = 0
            while i < len(self.fft) and not self.kill_received:
                end = time.time()
                i = int((end - start)/.25)
                state = self.getState(self.fft[i])
                self.color(state)
                time.sleep(.2)
                
        except Exception, e:
            print 'Unexpected error occurred', e
    
        finally:

            # Should finally clean up 
            GPIO.cleanup()