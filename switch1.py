import RPi.GPIO as IoPort
import time

Led1 = 18
Led2 = 23

def DisplayState(st):
    if st == 1:
        IoPort.output(Led1, False)
        IoPort.output(Led2, False)
    elif st == 2:
        IoPort.output(Led1, True)
        IoPort.output(Led2, False)
    elif st == 3:
        IoPort.output(Led1, False)
        IoPort.output(Led2, True)
    elif st == 4:
        IoPort.output(Led1, True)
        IoPort.output(Led2, True)

key1 = 8
End = 7


IoPort.setmode(IoPort.BCM)
IoPort.setup(Led1, IoPort.OUT)
IoPort.setup(Led2, IoPort.OUT)
IoPort.setup(key1, IoPort.IN)
IoPort.setup(End, IoPort.IN)

State = 1

while State <= 4:
    DisplayState(State)

    while True:
        if not IoPort.input(key1):
            break
        time.sleep(0.01)

    while True:
        if IoPort.input(key1):
            break

        time.sleep(0.01)

    State += 1


DisplayState(1)