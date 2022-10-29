import pygame
from djitellopy import tello
import cv2
me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False;
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True;
    pygame.display.update()
    return ans

def main():
    print(getKey("a"))

if __name__ == '__main__':
    init()
    while True:
        main()


while True:
    img = me.get_frame_read().frame
    img = cv2.rsize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)