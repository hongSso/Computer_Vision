import cv2 as cv
cap = cv.VideoCapture('hello.mp4')

if not cap.isOpened():
    print("error")
    exit()

print("frame width",int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print("frame height",int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print("frame count",int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps=cap.get(cv.CAP_PROP_FPS)
print('FPS:',fps)
delay=round(1000/fps)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    incersed=~frame
    cv.imshow('frame', frame)
    cv.imshow('inversed', incersed)

    if cv.waitKey(10) ==27:
        break

cv.destroyAllWindows()