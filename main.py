import keyin as k
import face_API as face
import pre_process as pp
import attendence as at
import catch

import threading

import time


def photo():
  for i in range(3):
    catch.takephoto()

# manual put id 

# k.updateID()

def roll():
  at.entercourse('大创中期会议')
  at.rollcall('test.jpg')