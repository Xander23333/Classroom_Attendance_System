import cv2
import time

def opencamera(): # Tested
  cap = cv2.VideoCapture(0)
  while(cap.isOpened()):
    # time.sleep(3)
    ret,frame = cap.read()
    if ret:
      cv2.imshow('frame',frame)
      cv2.imwrite('test.jpg',frame)
    else:
      print("camera read error!")
      break
    if cv2.waitKey(1) & 0xFF == ord('q'):
      print("manuallly quit")
      cap.release()
      break

import os
cnt = -1
def findname(): # Tested
  global cnt
  if cnt!=-1:
    cnt+=1
    return cnt
  else: 
    for root,dirs,files in os.walk('test_datas'): # Tested
      for img in files:
        filename,extention = os.path.splitext(img)
        if extention in ('.jpg','.jpeg','.png'):
          try:
            cnt = max(cnt,int(filename))
          except ValueError:
            continue
    cnt+=1
    return cnt

def takephoto():
  name = findname()
  cap = cv2.VideoCapture(0)
  if cap.isOpened():
    for i in range(4):
      print("\r{}".format(3-i),end='')
      time.sleep(1)
    print("\r",end='')
    ret,frame = cap.read()
    if ret:
      cv2.imwrite('test_datas/{}.jpg'.format(name),frame)
      print("takephoto success")    
    else:
      print("takephoto fail")
    cap.release()
