import numpy as np
import cv2
import random

global src_hsv
# def hue_changed(_=None):
#
#     lower_hue = cv2.getTrackbarPos('Lower Hue', 'mask')
#     upper_hue = cv2.getTrackbarPos('Upper Hue', 'mask')
#
#     lowerb = (lower_hue, 80, 100)
#     upperb = (upper_hue, 255, 255)
#     mask = cv2.inRange(src_hsv, lowerb, upperb)
#     print(lowerb)
#     print(upperb)
#
#     cv2.imshow('mask', mask)

# global src_hsv
src = cv2.imread('img4_1.png', cv2.IMREAD_COLOR)

if src is None:
    print('None')
    exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(src_hsv, (0, 80, 100), (179, 255, 255))
cv2.imshow('src', src)
cv2.imshow('mask', mask)
# cv2.namedWindow('mask')
# cv2.createTrackbar('Lower Hue', 'mask', 40, 179, hue_changed)
# cv2.createTrackbar('Upper Hue', 'mask', 80, 179, hue_changed)
# hue_changed(0)
cv2.waitKey()
cv2.destroyAllWindows()