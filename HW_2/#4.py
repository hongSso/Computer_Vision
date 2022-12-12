import numpy as np
import cv2
import random

src1 = cv2.imread('img4_1.png', cv2.IMREAD_COLOR)

if src1 is None:
    print('Image load failed!')
    exit()

src = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

dst_nor = cv2.normalize(src, None, -200, 255, cv2.NORM_MINMAX)
circles1 = cv2.HoughCircles(dst_nor, cv2.HOUGH_GRADIENT, 1, 6, param1=290, param2=21)
dst_nor_color = cv2.cvtColor(dst_nor, cv2.COLOR_GRAY2BGR)

circle =[]
count1=1

if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in range(circles1.shape[1]):
        cx, cy, radius = circles1[0][i]

        if radius > 12 or radius < 7:
            continue

        cv2.circle(dst_nor_color, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        circle.append([cx, cy])

        count1=count1+1

dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 6)
dst1 = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, None)
contours, hr = cv2.findContours(dst1, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt, labels, stats, controids = cv2.connectedComponentsWithStats(dst)
dst2 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)

final = []
count=0

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    if w < 70 or h<20 or area <1000 or w > 300 or h>200 or area >24000 :
        continue

    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv2.rectangle(dst2, pt1, pt2, (0,0, 255))
    final.append(0)

    for j in range(0, len(circle)):
        if x < circle[j][0] < x + w and y < circle[j][1] < y + h:
            final[count] = final[count] + 1

    count = count+1

final.sort()
print(final)

cv2.imshow('src1', src1)
cv2.imshow('dst_nor', dst_nor)
cv2.imshow('dst_nor_color', dst_nor_color)
cv2.imshow('dst', dst2)

if cv2.waitKey() == 27:
    exit()
cv2.destroyAllWindows()
