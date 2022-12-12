import numpy as np
import cv2

src1 = cv2.imread('img4_1.png', cv2.IMREAD_GRAYSCALE)

blur1 = cv2.blur(src1,(3,3))
circles1 = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT, 1, 20, param1=150, param2=50)

dst1 = cv2.cvtColor(blur1, cv2.COLOR_GRAY2BGR)

count1=1
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in range(circles1.shape[1]):
        cx, cy, radius = circles1[0][i]
        cv2.circle(dst1, (cx, cy), radius, (0, 0, 255), 2,  cv2.LINE_AA)
        print(count1)
        count1=count1+1
        # cv2.waitKey(0) & 0xFF == ord('a')

        cv2.imshow('dst1', dst1)
        if cv2.waitKey(3000) == 27:

            break
print("\n")

# cv2.imshow('src1', src1)
# cv2.imshow('dst1', dst1)


# cv2.waitKey()
cv2.destroyAllWindows()

