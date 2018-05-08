import face_API as face

tls = face.detect('xu0.jpg')
face.setuserid(tls[0], ID = '001')
face.single_addface('xu0.jpg','1011161122')
face.multi_search('xu0.jpg')
face.single_search("3abd841b64c3f2d25a6328f3a5431679")
ls = face.detect('/Users/xander/Documents/code/classroom_recognization_system/test_datas/3.jpg')
print(face.single_search(ls[0]))
