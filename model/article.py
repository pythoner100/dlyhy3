#coding:utf8
from util.database import get_db
from user import UserModel

class ArticleModel(object):
    def create_article(self,title, content, uid):
        db = get_db()
        data = db.insert("insert into article value (%s, %s, %s, %s, %s)", None, title, content, None, uid)
        db.close()
        return data


    def get_articles(self):
        db = get_db()
        articles = db.query('select * from article order by created_at ASC')
        for article in articles:
            uid = article.uid
            user_model = UserModel()
            user_info = user_model.get_user_info_by_id(uid)
            article['user_info'] = user_info
        db.close()
        return articles

    def get_hour_articles(self):
        db = get_db()
        articles = db.query('select * from article order by created_at DESC')
        for article in articles:
            uid = article.uid
            user_info = db.get('select id,username from user where id=%s',uid)
            article['user_info'] = user_info
        db.close()
        return articles

    def get_hot_articles(self):
        db = get_db()
        articles = db.query('select a.*,  (select count(*) from comment where comment.article_id=a.id) as count from article as a order by count DESC')
        for article in articles:
            uid = article.uid
            user_info = db.get('select * from user where id=%s',uid)
            article['user_info'] = user_info
        db.close()
        return articles

    def get_article_id(self, article_id):
        db = get_db()
        article = db.get('select * from article where id=%s',article_id)
        db.close()
        return article

    
        
