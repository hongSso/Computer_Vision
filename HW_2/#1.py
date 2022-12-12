import numpy as np
import cv2

src1 = cv2.imread('dice1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('dice2.png', cv2.IMREAD_GRAYSCALE)
src3 = cv2.imread('dice3.png', cv2.IMREAD_GRAYSCALE)
src4 = cv2.imread('dice4.png', cv2.IMREAD_GRAYSCALE)

if src1 is None:
    print('Image load failed!')
    exit()

if src2 is None:
    print('Image load failed!')
    exit()

if src3 is None:
    print('Image load failed!')
    exit()

if src4 is None:
    print('Image load failed!')
    exit()

blur1 = cv2.blur(src1,(3,3))
blur2 = cv2.blur(src2,(3,3))
blur3 = cv2.blur(src3,(3,3))
blur4 = cv2.blur(src4,(3,3))
circles1 = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30)
circles2 = cv2.HoughCircles(blur2, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30)
circles3 = cv2.HoughCircles(blur3, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30)
circles4 = cv2.HoughCircles(blur4, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30)

dst1 = cv2.cvtColor(blur1, cv2.COLOR_GRAY2BGR)
dst2 = cv2.cvtColor(blur2, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(blur3, cv2.COLOR_GRAY2BGR)
dst4 = cv2.cvtColor(blur4, cv2.COLOR_GRAY2BGR)

count1=0
count2=0
count3=0
count4=0

print("주사위1의 눈")
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in range(circles1.shape[1]):
        cx, cy, radius = circles1[0][i]
        cv2.circle(dst1, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        count1=count1+1
print(count1)
print("\n")

print("주사위2의 눈")
if circles2 is not None:
    circles2 = np.uint16(np.around(circles2))
    for i in range(circles2.shape[1]):
        cx, cy, radius = circles2[0][i]
        cv2.circle(dst2, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        count2=count2+1
print(count2)
print("\n")

print("주사위3의 눈")
if circles3 is not None:
    circles3 = np.uint16(np.around(circles3))
    for i in range(circles3.shape[1]):
        cx, cy, radius = circles3[0][i]
        cv2.circle(dst3, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        count3=count3+1
print(count3)
print("\n")

print("주사위4의 눈")
if circles4 is not None:
    circles4 = np.uint16(np.around(circles4))
    for i in range(circles4.shape[1]):
        cx, cy, radius = circles4[0][i]
        cv2.circle(dst4, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        count4=count4+1
print(count4)
print("\n")

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

if cv2.waitKey() == 27:
    exit()
cv2.destroyAllWindows()