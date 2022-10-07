import numpy as np
import cv2

img = np.full((200, 640, 3), 255, np.uint8)

text = "Hello, OpenCV"
fontFace = cv2.FONT_HERSHEY_TRIPLEX
fontScale = 2.0
thickness = 1

sizeText, _ = cv2.getTextSize(text, fontFace, fontScale, thickness)

org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] + sizeText[1]) // 2)
cv2.putText(img, text, org, fontFace, fontScale, (255, 0, 0), thickness)
cv2.rectangle(img, org, (org[0] + sizeText[0], org[1] - sizeText[1]), (0, 255, 0), 1)


cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()