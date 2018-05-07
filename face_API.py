#face_rec.py
import threading

API_secret = 'QDpN35MX7OGGLK0TRuEPjwxYMO35KxwT'
API_key = '1RuUWbO531XgelX7QH1Ktr0frJA2XrC_'
outer_id = 'datas'

API0_key = 'wZulEh6shrBv3kJyENxBx9ikU4M_qXra'
API0_secret = 'duek1s3zJ4p3YwlsHUY8guAi6yJ3_iv0'

d = {'api_key':API_key, 'api_secret':API_secret}
d0 = {'api_key':API0_key, 'api_secret':API0_secret}

addface_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
detect_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
getdetail_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
facesetcreat_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
setuserid_url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
search_url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
removefaceset_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'

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
  except Exception as e:
    print("detect error: {} !".format(e))
    return False
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
  except Exception as e:
    print("set ID error: {} !".format(e))
  else:
    print("set ID success!")


def single_addface(img_url, ID):# Tested
  # input a single-face photo + an ID to the faceset
  ls = detect(img_url)
  if ls == False:
    print('{} detect failed'.format(img_url))
    return
  setuserid(ls[0],ID)
  try:   
    data = {'outer_id':outer_id, 'face_tokens':ls[0]}
    data.update(d)
    r = requests.post(addface_url, data = data)
    r.raise_for_status()
  except Exception as e:
    print("addface error: {} !".format(e))
  else:
    print("addface success!")

def single_search(face_token):# Tested
  # single search in faceset  
  try:   
    data = {'outer_id':outer_id, 'face_token':face_token}
    data.update(d)
    r = requests.post(search_url, data = data)
    r.raise_for_status()
  except Exception as e:
    print("search error: {} !".format(e))
    return False
  else:
    print("search success!")

  dic = json.loads(r.text)
  pre_conf = dic["thresholds"]["1e-5"]
  real_conf = dic["results"][0]["confidence"]
  if real_conf<pre_conf:
    return False
  else:
    ID = dic["results"][0]["user_id"]
    print('{} has been found, the confidence is {}'.format(ID,real_conf))
    return ID

def multi_search(img_url):# 
  # multi persons photo to search, return a ID list
  ls = detect(img_url)
  id_list = []
  for i in ls:
    result = single_search(i)
    if result != False:
      id_list.append(result)
  return id_list

def getdetail(f = 'detail.json'):# Tested
  try:   
    data = {'outer_id':outer_id}
    data.update(d)
    r = requests.post(getdetail_url, data = data)
    r.raise_for_status()
  except Exception as e:
    print("getdetail error: {} !".format(e))
    return 
  else:
    print("getdetail success!")

  dic = json.loads(r.text)
  with open(f,'w') as fp:
    json.dump(dic, fp, indent = 2)
  print('success!')

def clear_faceset(): # Tested
  try:   
    data = {'outer_id':outer_id, 'face_tokens':'RemoveAllFaceTokens'}
    data.update(d)
    r = requests.post(removefaceset_url, data = data)
    r.raise_for_status()
  except Exception as e:
    print("clear error: {} !".format(e))
  else:
    print("clear success!")

