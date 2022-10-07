import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

cv2.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
cv2.rectangle(img, (50, 150), (150, 200), (0, 0, 128), -1)

cv2.circle(img, (300, 120), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 120), 60, (255, 0, 0), 3, cv2.LINE_AA)

cv2.ellipse(img, (120, 300), (60, 30), 20, 0, 270, (255, 255, 0), cv2.FILLED, cv2.LINE_AA)
cv2.ellipse(img, (120, 300), (100, 50), 20, 0, 360, (0, 255, 0), 2, cv2.LINE_AA)

pts = np.array([[250, 250], [300, 250], [300, 300], [350, 300], [350, 350], [250, 350]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()