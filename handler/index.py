#coding:utf8
import tornado.web
import torndb

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        db = torndb.Connection(host = "localhost", database = "hy3", user = "root", password = "11111111")
        articles = db.query("select * from article")
        username = self.get_cookie('username')
        user_id = self.get_cookie('id')
        for article in articles:
            uid = article.uid
            user_info = db.get("select id,username from user where id=%s", uid)
            article["user_info"] = user_info
        db.close()
        self.render("index.html",articles = articles, username = username, user_id = user_id)

