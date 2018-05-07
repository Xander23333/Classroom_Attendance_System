# make the size of photo <= 2Mb(2000*2000) 

import os
data_path = '/Users/xander/Documents/code/classroom_recognization_system/datas'
test_path = '/Users/xander/Documents/code/classroom_recognization_system/test_datas'
from PIL import Image

def small(img_url):
  with Image.open(img_url) as im:
    width,height = im.size
    m = max(width,height)
    width = int(width/m*2000)
    height = int(height/m*2000)
    im = im.resize((width,height))
    im.save(img_url)

def small_paths(paths):
  for root,dirs,files in os.walk(paths):
    for img in files:
      filename,extention = os.path.splitext(img)
      if extention in ('.jpg','.jpeg','.png'):
        img_url = os.path.join(root,img)
        fsize = os.path.getsize(img_url)
        if (fsize > 1.8*1024*1024):
          small(img_url)

def small_datas():
  small_paths(data_path)
  small_paths(test_path)
  print('datas standarlization finished')