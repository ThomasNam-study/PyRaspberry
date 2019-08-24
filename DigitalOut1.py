import RPi.GPIO as IoPort
import time
IoPort.setmode(IoPort.BCM)

led = 18

IoPort.setup(led, IoPort.OUT)

delays = [2.4, 0.4, 0.4, 0.4, 0.4, 0.4, 1.2, 1.2, 0.4, 1.2, 0.4, 1.2, 1.2, 0.4, 0.4, 0.4, 0.4, 0.4, 1.2]

onoff = False

def LedOn(port, delayV):
    IoPort.output(led, True)
    time.sleep(delayV)

def LedOff(port, delayV):
    IoPort.output(led, False)
    time.sleep(delayV)

def Send_S ():
    LedOn(led, 0.4)
    LedOff(led, 0.4)
    LedOn(led, 0.4)
    LedOff(led, 0.4)
    LedOn(led, 0.4)
    LedOff(led, 1.2)

LedOff(led, 2.4)
Send_S()