import numpy as np
import cv2
import random
# 넓은 면의 주사위 눈이 원에 제일 가까울 것이라는 가정
src1 = cv2.imread('img5.png', cv2.IMREAD_COLOR)

if src1 is None:
    print('Image load failed!')
    exit()

src = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 141, 20)
dst1 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, None)
circles1 = cv2.HoughCircles(dst1, cv2.HOUGH_GRADIENT, 1, 8, param1=210, param2=23)
dst_nor_color = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)

circle =[]
count1=0

if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in range(circles1.shape[1]):
        cx, cy, radius = circles1[0][i]

        if radius > 20 or radius < 7:
            continue
        cv2.circle(dst_nor_color, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        circle.append([cx, cy])
        count1=count1+1

cv2.imshow('dst_nor_color', dst_nor_color)
print(count1)

cv2.waitKey()
cv2.destroyAllWindows()
