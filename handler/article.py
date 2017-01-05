#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from base import BaseHandler


class ArticleHandler(BaseHandler):
    def get(self):
        self.render("article.html")

class ApiArticleHandler(BaseHandler):
    def post(self):
        uid = self.get_cookie('uid')
        if uid is None or uid == '':
            self.write('你还没登陆')
            return
                
        user = self.user_srv.get_user_article_by_uid(uid)
        if user is None:
           db.close()
           self.write('登录已经过期，请重新登录')
           return
    
        title = self.get_argument("title")
        content = self.get_argument("content")
        data = self.article_srv.create_article(title, content, uid)
        
        self.write('插入成功!文章ID是' + str(data))






