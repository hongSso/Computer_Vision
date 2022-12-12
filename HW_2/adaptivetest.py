import numpy as np
import cv2

src = cv2.imread('img4_1.png', cv2.IMREAD_GRAYSCALE)

blur = cv2.blur(src,(2,2))

dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 35, 9)
if src is None:
    print('wow')
    exit()


dst1 = cv2.dilate(dst, None)


cv2.imshow('src', blur)
cv2.imshow('dst', dst1)

cv2.waitKey()
cv2.destroyAllWindows()
