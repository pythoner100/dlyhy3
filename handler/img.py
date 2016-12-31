#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from model.img import ImgModel

class ImgHandler(tornado.web.RequestHandler):
    def get(self):
        db = get_db()
        img_model = ImgModel()
        yans = img_model.create_img()
        db.close()
        self.render("img.html",yans=yans)

class ApiImgHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        img = self.get_argument("img")
        db = get_db()
        img_model = ImgModel()
        yy = img_model.create_api_img(username, password, img)
        db.close()
        print (yy)
        self.write("插入成功!您的ID是" + str(yy))


