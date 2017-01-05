#coding:utf8
import tornado.web
import torndb

from util.database import get_db
from base import BaseHandler

class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

class ApiRegisterHandler(BaseHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        data = self.user_srv.get_user_register(username, password)
  
        self.write("注册成功!您的ID是" + str(data))

