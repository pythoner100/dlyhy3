#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from model.user import UserModel

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_cookie("username")
        self.render("login.html", username = username)

class ApiLoginHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = get_db()
        user_model = UserModel()
        data = user_model.get_user_by_username(username)
        data3 = user_model.get_user_by_password(username, password)
       
        db.close()
        if data3 is not None:
            self.set_cookie("username", username)
            self.set_cookie("uid", str(data3.id))
            self.set_cookie("id", str(data3.id))
            data2 = user_model.update_user_by_username(username)
            self.write("登录成功!您上次登录时间是" + str(data['last_login_at']))
        else:
            self.write("登录失败!请输入正确的用户名或密码!")




