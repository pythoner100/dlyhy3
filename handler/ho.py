#coding:utf8
import tornado.web
import torndb
#from model.article import ArticleModel
#from util.database import get_db

class HotHandler(tornado.web.RequestHandler):
    def get(self):
        #article_model = ArticleModel()
        #articles = article_model.get_articles_order_by_time()
        #db = get_db()
        db = torndb.Connection(host = "localhost", database = "hy3", user = "root", password = "11111111")
        articles = db.query("select a.*,  (select count(*) from comment where comment.article_id=a.id) as count from article as a  order by count desc")        
        for article in articles:
            uid = article.uid
            user_info = db.get("select id,username from user where id=%s", uid)
            article["user_info"] = user_info
        db.close()
        self.render("hot.html",articles=articles)

class HourHandler(tornado.web.RequestHandler):
    def get(self):
        #db = get_db()
        db = torndb.Connection(host = "localhost", database = "hy3", user = "root", password = "11111111")
        articles = db.query("select * from article order by created_at DESC")
        for article in articles:
            uid = article.uid
            user_info = db.get("select id,username from user where id=%s", uid)
            article["user_info"] = user_info
        db.close()
        #article_model = ArticleModel()
        #articles = article_model.get_all_articles_order_by_comment_count()
        self.render("hour.html",articles = articles)
                                                                                                 
