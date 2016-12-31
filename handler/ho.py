#coding:utf8
import tornado.web
import torndb

from model.article import ArticleModel


class HourHandler(tornado.web.RequestHandler):
    def get(self):
        article_model = ArticleModel()
        articles =article_model.get_hour_articles()

        self.render("hour.html",articles = articles)


class HotHandler(tornado.web.RequestHandler):
    def get(self):
        article_model = ArticleModel()
        articles = article_model.get_hot_articles()

        self.render("hot.html",articles=articles)

                                                                                                 
