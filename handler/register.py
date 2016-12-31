#coding:utf8
import tornado.web
import torndb

from util.database import get_db
from model.user import UserModel

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")

class ApiRegisterHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_model = UserModel()
        data = user_model.get_user_register(username, password)
  
        self.write("注册成功!您的ID是" + str(data))

