import cv2
import time
cap = cv2.VideoCapture(0)

cnt = 0
while(cap.isOpened()):
  time.sleep(3)
  ret,frame = cap.read()
  if ret:
    cv2.imshow('frame',frame)
    cv2.imwrite('xu{}.jpg'.format(cnt),frame)
    cnt += 1
    if cnt >= 1:
      break
  else:
    break
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
    