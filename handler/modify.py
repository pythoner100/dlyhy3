#coding:utf8
import tornado.web
import torndb

from util.database import get_db
from base import BaseHandler

class ModifyHandler(BaseHandler):
    def get(self):
        self.render("modify.html")

class ApiModifyHandler(BaseHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        password1 = self.get_argument("password1")
        data = self.user_srv.get_user_modify_data(username, password)
        if data is not None:
            data2 = self.user_srv.update_user_modify_data2(password1, username)
            self.write("密码修改成功!")
        else:
            self.write("密码修改失败,请输入正确的用户名或密码!")

