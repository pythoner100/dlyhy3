#coding:utf8
import tornado.web
import torndb

class ModifyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("modify.html")

class ApiModifyHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        password1 = self.get_argument("password1")
        db = torndb.Connection(host = "localhost", database = "hy3", user = "root", password = "11111111")
        data = db.get("select id from user where username = %s and password = %s", username,password)
        if data is not None:
            data2 = db.update("update user set password=%s where username = %s", password1, username)
            self.write("密码修改成功!")
        else:
            self.write("密码修改失败,请输入正确的用户名或密码!")
        db.close()  
