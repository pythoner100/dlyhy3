#coding:utf8
import tornado.web
import torndb
from model.index import get_hour_articles,get_hot_articles


class HourHandler(tornado.web.RequestHandler):
    def get(self):
        articles = get_hour_articles()

        self.render("hour.html",articles = articles)



class HotHandler(tornado.web.RequestHandler):
    def get(self):
        articles = get_hot_articles()

        self.render("hot.html",articles=articles)

                                                                                                 
