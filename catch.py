import cv2
import time

def opencamera(timesleep,times=1):
  cap = cv2.VideoCapture(0)
  cnt = 0
  while(cap.isOpened()):
    time.sleep(3)
    ret,frame = cap.read()
    if ret:
      cv2.imshow('frame',frame)
      cv2.imwrite('test.jpg',frame)
      cnt += 1
      if cnt >= 1:
        break
    else:
      break
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

opencamera(1)