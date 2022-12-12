import numpy as np
import cv2

src1 = cv2.imread('img4_1.png', cv2.IMREAD_GRAYSCALE)

# blur1 = cv2.blur(src1,(2,2))

# sharpening_mask1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# sharpening = cv2.filter2D(src1, -1, sharpening_mask1)
dst = cv2.normalize(src1, None, -200, 255, cv2.NORM_MINMAX)
circles1 = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT, 1, 5, param1=290, param2=18)

circle =[]
dst1 = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
print(circles1[0][1])
count1=1
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in range(circles1.shape[1]):
        cx, cy, radius = circles1[0][i]

        if radius > 12 or radius < 7:
            continue
        cv2.circle(dst1, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        circle.append([cx, cy])
        print(circle)
        # print(count1)
        # print(radius)
        count1=count1+1
print("\n")
print(len(circle))

cv2.imshow('src1', src1)
cv2.imshow('dst1', dst1)


cv2.waitKey()
cv2.destroyAllWindows()

