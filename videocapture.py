import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("error")
    exit()

print("frame width",int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print("frame height",int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
