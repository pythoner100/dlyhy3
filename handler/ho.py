#coding:utf8
import tornado.web
import torndb

from base import BaseHandler



class HourHandler(BaseHandler):
    def get(self):
        articles =self.article_srv.get_hour_articles()

        self.render("hour.html",articles = articles)


class HotHandler(BaseHandler):
    def get(self):
        articles =self.article_srv.get_hot_articles()

        self.render("hot.html",articles=articles)

                                                                                                 
