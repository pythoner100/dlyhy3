#coding:utf8
import tornado.web
import torndb

from util.database import get_db


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")

class ApiRegisterHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = get_db()
        data = db.insert("insert into user value(%s,%s,%s,%s,%s)", None,username,password,None,None)
        db.close()
        self.write("注册成功!您的ID是" + str(data))

