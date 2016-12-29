#coding:utf8
import tornado.web
import torndb
from util.database import get_db


class ArticleHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("article.html")

class ApiArticleHandler(tornado.web.RequestHandler):
    def post(self):
        uid = self.get_cookie('uid')
        if uid is None or uid == '':
            self.write('你还没登陆')
            return

        db = get_db()
        user = db.get('select id from user where id=%s', uid)
        if user is None:
            self.write('登录已经过期，请重新登录')
            return

        title = self.get_argument("title")
        content = self.get_argument("content")
        uid = self.get_cookie("uid")
        db = get_db()
        data = db.insert("insert into article value (%s,%s,%s,%s,%s)",None,title,content,None,uid)
        db.close()
        self.write('插入成功!文章ID是' + str(data))





