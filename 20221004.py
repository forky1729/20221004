import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
maxV = 3.3
comp = 4
troyka = 17
GPIO.setup(dac,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def n2d(decimal):
    signal = d2b(decimal)
    GPIO.output(dac, signal)
    return signal

    


#1
try:
    while True:
        for value in range (256):
            signal = n2d(value)
            voltage = value / levels * maxV
            time.sleep(0.0007)
            compV = GPIO.input(comp)
            if compV == 0:
                print(value, "   ", signal, "   ", voltage)
                break

finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
