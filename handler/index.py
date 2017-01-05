#coding:utf8
import tornado.web

from base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        username = self.get_cookie('username')
        user_id = self.get_cookie('id')
        articles =self.article_srv.get_articles()
        self.render('index.html',articles = articles, username = username, user_id = user_id)



