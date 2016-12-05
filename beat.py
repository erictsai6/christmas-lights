import RPi.GPIO as GPIO
import time
import threading

class Beat(threading.Thread):
    def __init__(self, x):
        self.__x = x
        threading.Thread.__init__(self)

    def shift_chords(self, chord):
        signal = GPIO.HIGH if chord == 0 else GPIO.LOW
        opposite_signal = GPIO.HIGH if signal == GPIO.LOW else GPIO.LOW
        GPIO.output(2, signal)
        GPIO.output(4, signal)
        GPIO.output(3, opposite_signal)
        GPIO.output(17, opposite_signal)

    def run(self):
        for i in range(0, 12):
            self.shift_chords(0)
            time.sleep(0.687)
            self.shift_chords(1)
            time.sleep(0.687)

