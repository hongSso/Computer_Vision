import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        break

    incersed=~frame
    cv.imshow('frame', frame)
    cv.imshow('inversed', incersed)

    if cv.waitKey(10) ==27:
        break

cv.destroyAllWinidows()