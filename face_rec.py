#face_rec.py
import threading

API_secret = 'QDpN35MX7OGGLK0TRuEPjwxYMO35KxwT'
API_key = '1RuUWbO531XgelX7QH1Ktr0frJA2XrC_'


API0_key = 'wZulEh6shrBv3kJyENxBx9ikU4M_qXra'
API0_secret = 'duek1s3zJ4p3YwlsHUY8guAi6yJ3_iv0'

d = {'api_key':API_key, 'api_secret':API_secret}
d0 = {'api_key':API0_key, 'api_secret':API0_secret}

addface_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
detect_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
getdetail_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
facesetcreat_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
setuserid_url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'

import requests
import json

def detect(img_url):# Tested
  # return a list of face_tokens
  try:
    fr = open(img_url,'rb')
    files = {'image_file':fr}
    data = {}
    data.update(d)
    r = requests.post(detect_url, data = data, files = files)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
  except:
    print("detect error!")
    return
  else:
    print("detect success!")
  finally:
    fr.close()

  ls = []
  dic = json.loads(r.text)
  for ddic in dic["faces"]:
    ls.append(ddic["face_token"])
  
  return ls

  """
  dic = json.loads(r.text)
  with open('detect.json','w') as fp:
    json.dump(dic, fp, indent = 2)
  print('success!')
  """

def setuserid(face_token, ID):# Tested
  try:
    data = {'face_token':face_token, 'user_id':ID}
    data.update(d)
    r = requests.post(setuserid_url, data = data)
    r.raise_for_status()
#    print(r.text)
  except:
    print("set ID error!")
  else:
    print("set ID success!")


def single_addface(img_url, ID):# Tested
  # input a single-face photo + an ID to the faceset
  ls = detect(img_url)
  setuserid(ls[0],ID)
  try:   
    data = {'outer_id':'datas', 'face_tokens':ls[0]}
    data.update(d)
    r = requests.post(addface_url, data = data)
    r.raise_for_status()
  except:
    print("addface error!")
  else:
    print("addface success!")

for i in range(5):
  single_addface('xu{}.jpg'.format(i),'1011161122')


