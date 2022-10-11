import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
levels = 2**bits
maxV = 3.3
comp = 4
troyka = 17
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def n2d(value):
    signal = d2b(value)
    GPIO.output(dac, signal)
    return signal


def adc1():
    for value in range (256):
            signal = n2d(value)
            time.sleep(0.0007)
            compV = GPIO.input(comp)
            if compV == 0:
                return value
                break


def adc2():
    res_value = 0
    for i in range (7,-1, -1):
        signal = n2d(res_value)
        value = res_value + 2**i-1
        time.sleep(0.00005)
        compV = GPIO.input(comp)
        if compV != 0:
            res_value += 2**i
    return res_value



#1
try:
    while True:
        #print(adc1()*3.3/256)
        #print(adc2()*3.3/256)
        if adc1()/256==1:
            GPIO.output(leds, [1,1,1,1,1,1,1,1])
        elif adc1()/256>=7/8 and adc1()/256<1:
            GPIO.output(leds, [0,1,1,1,1,1,1,1])
        elif adc1()/256>=6/8 and adc1()/256<7/8:
            GPIO.output(leds, [0,0,1,1,1,1,1,1])
        elif adc1()/256>=5/8 and adc1()/256<6/8:
            GPIO.output(leds, [0,0,0,1,1,1,1,1])
        elif adc1()/256>=4/8 and adc1()/256<5/8:
            GPIO.output(leds, [0,0,0,0,1,1,1,1])
        elif adc1()/256>=3/8 and adc1()/256<4/8:
            GPIO.output(leds, [0,0,0,0,0,1,1,1])
        elif adc1()/256>=2/8 and adc1()/256<3/8:
            GPIO.output(leds, [0,0,0,0,0,0,1,1])
        elif adc1()/256>=1/8 and adc1()/256<2/8:
            GPIO.output(leds, [0,0,0,0,0,0,0,1])
        else:
            GPIO.output(leds, [0,0,0,0,0,0,0,0])

finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
