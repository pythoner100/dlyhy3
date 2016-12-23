#coding:utf8
import tornado.web
import torndb

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_cookie("username")
        self.render("login.html", username = username)

class ApiLoginHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = torndb.Connection(host = "localhost",database="hy3",user = "root", password ="11111111",time_zone='+8:00')
        data = db.get("select last_login_at from user where username=%s", username)
        data2 = db.update("update user set last_login_at = NULL where username = %s", username)
        data3 = db.get("select id from user where username=%s and password = %s",username,password)
        db.close()
        if data3 is not None:
            self.set_cookie("username", username)
            self.set_cookie("uid", str(data3.id))
            self.set_cookie("id", str(data3.id))
            self.write("登录成功!您上次登录时间是" + str(data['last_login_at']))
        else:
            self.write("登录失败!请输入正确的用户名或密码!")




