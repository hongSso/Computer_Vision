import numpy as np
import cv2
import random

src = cv2.imread('dices.png', cv2.IMREAD_GRAYSCALE)


blur = cv2.blur(src,(4,4))

edge = cv2.Canny(blur, 200, 300)
contours, hello = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(len(contours))
print(hello[0])
dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

for i in range(len(contours)):
    c = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))
    cv2.drawContours(dst, contours, i, c, 2)
    cv2.imshow('dst', dst)


cv2.imshow('src', edge)
cv2.waitKey()
cv2.destroyAllWindows()