import numpy as np
import cv2
import random
src = cv2.imread('img4_4.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('wow')
    exit()

# cv2.imshow('src', src)
blur = cv2.blur(src, (7,10))
# _, dst = cv2.threshold(src,120,255, cv2.THRESH_BINARY)
# dst1 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
dst1 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,93,10)
# dst1 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 23, 3)
dst = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)

cnt, labels, stats, controids = cv2.connectedComponentsWithStats(dst)
# cv2.imshow('dst', dst)
dst1 = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
count=0
for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    if w < 70 or h<20 or area <1000 or w > 300 or h>200 or area >24000 :
        continue
    # elif area > 10000:
    #     continue
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv2.rectangle(dst1, pt1, pt2, (0,0, 255))
    count= count+1



cv2.imshow('blur', dst)
cv2.imshow('blur', dst1)

cv2.waitKey()
cv2.destroyAllWindows()
