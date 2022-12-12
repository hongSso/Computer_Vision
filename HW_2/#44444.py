import numpy as np
import cv2

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv2.rectangle(img, pt1, pt2, (0,155,255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255))

img = cv2.imread('img4_1.png', cv2.IMREAD_COLOR)
cv2.imshow('src', img)
img = cv2.blur(img,(3,3))
# circles1 = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT, 1,5, param1=300, param2=40)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for pts in contours:
    if cv2.contourArea(pts) <400:
        continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    vtc = len(approx)

    if vtc == 3:
        setLabel(img, pts, 'TRI')
    elif vtc == 4:
        setLabel(img, pts, 'RECT')
    else:
        lenth = cv2.arcLength(pts, True)
        area = cv2.contourArea(pts)
        ratio = 4. * 3.14 * area / (lenth * lenth)

        if ratio > 0.05:
            setLabel(img, pts, 'CIR')

# count1=1
# if circles1 is not None:
#     circles1 = np.uint16(np.around(circles1))
#     for i in range(circles1.shape[1]):
#         cx, cy, radius = circles1[0][i]
#         cv2.circle(dst1, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
#         print(count1)
#         count1=count1+1
# print("\n")

# cv2.imshow('src1', src1)
cv2.imshow('img', img)



cv2.waitKey()
cv2.destroyAllWindows()

