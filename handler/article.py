#coding:utf8
import tornado.web
import torndb

class ArticleHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("article.html")

class ApiArticleHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument("title")
        content = self.get_argument("content")
        uid = self.get_cookie("uid")
        db = torndb.Connection(host = "localhost",database = "hy3",user = "root",password = "11111111",time_zone = '+8:00')
        data = db.insert("insert into article value (%s,%s,%s,%s,%s)",None,title,content,None,uid)
        db.close()
        self.write('插入成功!文章ID是' + str(data))





