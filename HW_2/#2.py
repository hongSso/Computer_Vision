import numpy as np
import cv2
import random

src = cv2.imread('dices.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

def saturated(value):
    if value > 128:
        value = 255
    elif value <= 128:
        value = 0
    return value

blur = cv2.blur(src,(4,4))

for y in range(blur.shape[0]):
    for x in range(blur.shape[1]):
        blur[y, x] = saturated(blur[y, x])

contours, hello = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
dst = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
for i in range(len(contours)):
    cv2.drawContours(dst, contours, i, (0,0,255), 2)

count=[]
num=1
k=0
index=0

while k < (len(contours)):
    if hello[0][k][3] == -1:
        count.append(1)
        move=hello[0][k][2]
        while hello[0][move][0] != -1: #1
            num=num+1
            move=hello[0][move][0]
        count[index]=num
        k=move+1
        index=index+1
        num=1
    else:
        k=k+1

count.sort()
print(count)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

if cv2.waitKey() == 27:
    exit()
cv2.destroyAllWindows()