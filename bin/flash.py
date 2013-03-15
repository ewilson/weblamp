import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def switch(on):
    GPIO.output(11,on)

def read():
    return GPIO.input(11)
    
