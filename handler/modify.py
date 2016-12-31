#coding:utf8
import tornado.web
import torndb

from util.database import get_db
from model.user import UserModel

class ModifyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("modify.html")

class ApiModifyHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        password1 = self.get_argument("password1")
        db = get_db()
        user_model = UserModel()
        data = user_model.get_user_modify_data(username, password)
        if data is not None:
            data2 = user_model.update_user_modify_data2(password1, username)
            self.write("密码修改成功!")
        else:
            self.write("密码修改失败,请输入正确的用户名或密码!")
        db.close()  
