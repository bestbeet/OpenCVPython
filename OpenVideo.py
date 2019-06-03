import cv2

cap = cv2.VideoCapture("Video.mp4")
while (True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Show camera',gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
