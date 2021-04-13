import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    rz = cv2.resize(frame, (int(frame.shape[0] * 0.72), int(frame.shape[1] * 0.72)), interpolation=cv2.INTER_AREA)

    cv2.imshow('frame', frame)
    cv2.imshow('resize', rz)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindow()
