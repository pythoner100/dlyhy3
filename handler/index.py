#coding:utf8
import tornado.web

from model.index import get_articles


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        articles = get_articles()
        self.render('index.html',articles = articles)



