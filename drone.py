from djitellopy import tello
import cv2
import pygame
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if getKey("RIGHT"): lr = speed
    elif getKey("LEFT"): lr = -speed

    if getKey("UP"): ud = speed
    elif getKey("DOWN"): ud = -speed

    if getKey("a"): yv = speed
    elif getKey("d"): yv = -speed

    if getKey("w"): ud = speed
    if getKey("s"): ud = -speed

    if getKey("t"): me.takeoff()
    elif getKey("l"): me.land()

    return [lr, fb, ud, yv]

def main():
    init()
    while True:
        vals = getKeyboardInput()
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        sleep(0.05)