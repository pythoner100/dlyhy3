#coding:utf8
from util.database import get_db
from base import BaseModel

class ImgModel(object):
    def create_img(self):
        self.db = get_db()
        yans = self.db.query("select * from yan")
        self.db.close()
        
        return yans

    def create_api_img(self, username, password, img):
        self.db = get_db()
        yy = self.db.insert("insert into yan value(%s, %s, %s, %s, %s)",None, username, password, img, None)
        self.db.close()
   
        return yy
    
