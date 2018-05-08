import face_API as face
import pymysql as pl
import pre_process as pp
import json

infodict = {}

def entercourse(coursename):# Tested
  db = pl.connect(host="rm-m5ec899sxqwx2rc9tgo.mysql.rds.aliyuncs.com",
                      user="root", password="Aa123456", db="classroom", charset='utf8')
  cur = db.cursor()

  findid = "select courseid from courses where coursename=\"{}\"".format(coursename)
  cur.execute(findid)
  try:
    courseid = cur.fetchone()[0]
  except TypeError:
    print("No such a course!")
    return

  select = "select id from {}".format(courseid)
  cur.execute(select)
  idlist = []
  for i in cur.fetchall():
    idlist.append(i[0])

  global infodict
  for ID in idlist:
    getinfo = "select * from students where ID=\"{}\"".format(ID)
    cur.execute(getinfo)
    lls = cur.fetchall()[0]
    infodict[lls[0]] = {'name':lls[1], 'class':lls[2]}
  # print(infodict)
  cur.close()
  db.close()

def rollcall(img_url):
  # return json
  global infodict

  pp.small(img_url)
  ls = face.multi_search(img_url)

  donels, undonels = [],[]
  for i in infodict:
    if i in ls:
      donels.append(i)
    else:
      undonels.append(i)
  
  dic = {}
  dic["donenumber"] = len(donels)
  dic["undonenumber"] = len(undonels)
  dic["done"] = form(donels)
  dic["undone"] = form(undonels)
  with open("display/rollcall.json","w") as fp:
    json.dump(dic, fp, ensure_ascii=False, indent = 2)

def form(ls):# Tested
  global infodict
  dic = {}
  for ID in ls:
    cl = infodict[ID]['class']
    if cl not in dic:
      dic[cl] = {}
    dic[cl][ID] = infodict[ID]['name']
  return dic

