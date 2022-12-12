import numpy as np
import cv2

# 1. 넓은 면의 주사위 눈이 원에 제일 가까울 것이라는 가정
src1 = cv2.imread('img5.png', cv2.IMREAD_COLOR)

if src1 is None:
    print('Image load failed!')
    exit()

def saturated(value):
    if value > 210:
        value = 255
    elif value <= 210:
        value = 0
    return value

src = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
dst_1 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 141, 20)
dst1_1 = cv2.morphologyEx(dst_1, cv2.MORPH_OPEN, None)
circles1 = cv2.HoughCircles(dst1_1, cv2.HOUGH_GRADIENT, 1, 8, param1=210, param2=23)
dst1_color = cv2.cvtColor(dst1_1, cv2.COLOR_GRAY2BGR)

circle =[]
count1=0

if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in range(circles1.shape[1]):
        cx, cy, radius = circles1[0][i]

        if radius > 20 or radius < 7:
            continue
        cv2.circle(dst1_color, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        circle.append([cx, cy])
        count1=count1+1


# 2. 밝은 면이 가장 넓은 면일거라는 가정
blur = cv2.blur(src,(10,10))

for y in range(blur.shape[0]):
    for x in range(blur.shape[1]):
        blur[y, x] = saturated(blur[y, x])

contours, hello = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
dst_2 = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

for i in range(len(contours)):
    cv2.drawContours(dst_2, contours, i, (0,0,255), 2)

count=[]
num=1
k=0
index=0

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

count.sort()
print("case1 : "+str(count[0]))

cv2.putText(dst1_color, "#1 Close to the circle", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)
cv2.putText(dst_2, "#2 The bright side is wide", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)
cv2.imshow('dst1', dst1_color)
cv2.imshow('dst2', dst_2)
print("case2 : "+str(count1))

cv2.waitKey()
cv2.destroyAllWindows()
