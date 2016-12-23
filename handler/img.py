#coding:utf8
import tornado.web
import torndb
class ImgHandler(tornado.web.RequestHandler):
    def get(self):
        db = torndb.Connection(host = "localhost",database = "hy",user = "root" ,password = "11111111")
        yans = db.query("select * from yan")
        db.close()
        self.render("img.html",yans=yans)


class ApiImgHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        img = self.get_argument("img")
        db = torndb.Connection(host = "localhost",database = "hy",user = "root",password = "11111111")
        yy = db.insert("insert into yan value(%s,%s,%s,%s,%s)",None,username,password,img,None)
        db.close()
        print (yy)
        self.write("插入成功!您的ID是" + str(yy))


