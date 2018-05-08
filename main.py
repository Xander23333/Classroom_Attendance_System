import keyin
import face_API as face
import pre_process as pp
import attendence as at

import threading

import time

at.entercourse('实验室')

cnt = 0
while(True):
    pp.small('test.jpg')
    at.rollcall('test.jpg')
    time.sleep(5)
    cnt+=1
    if cnt>10:
      break




