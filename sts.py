import explorerhat
import time

# Move the STS around in a circle, because who wants to
# go somewhere anyway
def circle():
    explorerhat.motor.one.forwards()
    explorerhat.motor.two.backwards()

def stop():
    explorerhat.motor.one.speed(0)
    explorerhat.motor.two.speed(0)

def moveForward():
    explorerhat.motor.one.forwards()
    explorerhat.motor.two.forwards()

# Explore!
circle()
while True:
    stop()
    time.sleep(3)
    circle()
    time.sleep(1)
    moveForward()
    time.sleep(2)
