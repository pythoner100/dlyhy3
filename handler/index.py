#coding:utf8
import tornado.web


from model.article import ArticleModel


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_cookie('username')
        user_id = self.get_cookie('id')
        article_model = ArticleModel()
        articles =article_model.get_articles()
        self.render('index.html',articles = articles, username = username, user_id = user_id)



