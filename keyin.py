# input the photo in datas to faceset, set ID as its dir name
import os
from os import path
import face_API as face

data_path = '/Users/xander/Documents/code/classroom_recognization_system/datas'

def updateall():
  face.clear_faceset()
  os.chdir(data_path)
  pa = os.getcwd()
  for ID in os.listdir(pa):
    try:  # all ID is int number
      int(ID)
    except ValueError:
      continue
    else:
      imgpath = path.join(pa,ID)
      for img in os.listdir(imgpath):
        (filename,extension) = path.splitext(img)
        if extension in ('.jpg','.jpeg','.png'):
          face.single_addface(img_url = path.join(imgpath,img) , ID = ID)

def updateID(ID):
  try:
    int(ID)
  except (ValueError,FileNotFoundError):
    print("No such an ID!")
    return
  else:
    imgpath = path.join(data_path,ID)
    for img in os.listdir(imgpath):
      (filename,extension) = path.splitext(img)
      if extension in ('.jpg','.jpeg','.png'):
        face.single_addface(img_url = path.join(imgpath,img) , ID = ID)




