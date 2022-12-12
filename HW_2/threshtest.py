import numpy as np
import cv2
import random
src = cv2.imread('img4_1.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('wow')
    exit()

cv2.imshow('src', src)
_, dst = cv2.threshold(src, 85,200, cv2.THRESH_TOZERO)
# cv2.imshow('dst', dst)

blur = cv2.blur(dst,(4,4))

# contours, hello = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# dst = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
# for i in range(len(contours)):
#     c = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))
#     cv2.drawContours(dst, contours, i, c, 2)

cv2.imshow('blur', dst)
cv2.waitKey()
cv2.destroyAllWindows()
