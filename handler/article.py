#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from model.article import ArticleModel


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
           db.close()
           self.write('登录已经过期，请重新登录')
           return
        db.close()
        title = self.get_argument("title")
        content = self.get_argument("content")
        article_model = ArticleModel()
        data =article_model.create_article(title, content, uid)
        
        self.write('插入成功!文章ID是' + str(data))






