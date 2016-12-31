#coding:utf8
from util.database import get_db

class ImgModel(object):
    def create_img(self):
        db = get_db()
        yans = db.query("select * from yan")
        db.close()
        
        return yans

    def create_api_img(self, username, password, img):
        db = get_db()
        yy = db.insert("insert into yan value(%s, %s, %s, %s, %s)",None, username, password, img, None)
        db.close()
   
        return yy
    
