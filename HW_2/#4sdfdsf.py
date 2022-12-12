import numpy as np
import cv2
import random

src = cv2.imread('img4_1.png', cv2.IMREAD_GRAYSCALE)


blur = cv2.blur(src,(5,5))

edge = cv2.Canny(blur, 150, 200)
contours, hello = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(len(contours))
print(hello[0])
dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

for i in range(len(contours)):
    c = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))
    cv2.drawContours(dst, contours, i, c, 2)



cv2.imshow('src', src)
cv2.imshow('edge', edge)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()