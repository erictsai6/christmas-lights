import pygame
import RPi.GPIO as GPIO
import time
from beat import Beat

GPIO.setmode(GPIO.BCM)

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

BEAT_WAIT = 0.687
pygame.mixer.init()
pygame.mixer.music.load('count-on-me.mp3')

try:

    pygame.mixer.music.play()

    # Starts background beat
    Beat(0).start() 

    time.sleep(5.34)
    # Starts melody 

    # if
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.30)

    # you
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.10)

    # e
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.15)
    # ver
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.10)

    # find
    GPIO.output(9, GPIO.LOW)
    time.sleep(0.17)

    # your
    GPIO.output(9, GPIO.HIGH)
    time.sleep(0.10)

    # self
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.17)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.17)
    GPIO.output(17, GPIO.HIGH)


    time.sleep(60)
    GPIO.cleanup()
    print "Good bye!"

except KeyboardInterrupt:
    print "quit"
    GPIO.cleanup()


