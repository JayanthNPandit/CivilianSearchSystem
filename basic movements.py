from djitellopy import tello
import cv2
import pygame
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
me.move_forward(30)
me.send_rc_control(50, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 30, 0, 0)
sleep(2)
me.send_rc_control(30, 50, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(2)
me.stream_on()

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


if __name__ == '__main__':
    init()
    while True:
        main();

while False:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

me.land()