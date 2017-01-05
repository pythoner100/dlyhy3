#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from base import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        username = self.get_cookie("username")
        self.render("login.html", username = username)

class ApiLoginHandler(BaseHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        data = self.user_srv.get_user_by_username(username)
        data3 = self.user_srv.get_user_by_password(username, password)
        if data3 is not None:
            self.set_cookie("username", username)
            self.set_cookie("uid", str(data3.id))
            self.set_cookie("id", str(data3.id))
            data2 = self.user_srv.update_user_by_username(username)
            self.write("登录成功!您上次登录时间是" + str(data['last_login_at']))
        else:
            self.write("登录失败!请输入正确的用户名或密码!")




