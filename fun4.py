import numpy as np
import cv2 as cv

def fun4():
    img1=cv.imread('15.jpg',cv.IMREAD_REDUCED_COLOR_2)

    img2=img1[200:400,200:400]

    img1[200:400,200:400] = 255-img2

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)

    cv.waitKey()
    cv.destroyAllWindows()


fun4()