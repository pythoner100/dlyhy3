#coding:utf8
import tornado.web
import torndb

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")

class ApiRegisterHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = torndb.Connection(host ="localhost", database = "hy3", user = "root", password = "11111111")
        data = db.insert("insert into user value(%s,%s,%s,%s,%s)", None,username,password,None,None)
        db.close()
        self.write("注册成功!您的ID是" + str(data))

