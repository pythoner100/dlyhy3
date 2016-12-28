#coding:utf8
import tornado.web
import torndb
#from model.article import ArticleModel
#from util.database import get_db

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
       # db = get_db()
     
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
        #article_model = ArticleModel()
        #articles = article_model.get_all_articles()
        #self.render('index.html', articles=articles)

