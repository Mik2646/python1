from windowCapture import *
import cv2 as cv
from myClassbot import *

windows = WindowCapture('Calculater')  

while True:

    screen = windows.screenshot()
    search = myClassbot()
    # print(screen)
    # cv.imshow('paint',screen)
    # cv.waitKey()
    # cv.destroyWindow()