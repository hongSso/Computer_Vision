import numpy as np
import cv2

def on_threshold(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_TRIANGLE)
    cv2.imshow('dst', dst)

filename = 'img4_1.png'

src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if src is None:
    print('wow')
    exit()

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos('Threshold', 'dst', 128)
cv2.waitKey()
cv2.destroyAllWindows()
