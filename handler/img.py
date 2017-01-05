#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from base import BaseHandler

class ImgHandler(BaseHandler):
    def get(self):
        yans = self.img_srv.create_img()
        self.render("img.html",yans=yans)

class ApiImgHandler(BaseHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        img = self.get_argument("img")
        yy = self.img_srv.create_api_img(username, password, img)
        print (yy)
        self.write("插入成功!您的ID是" + str(yy))


