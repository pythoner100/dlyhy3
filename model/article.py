#coding:utf8
from util.database import get_db
from user import UserModel
from base import BaseModel

class ArticleModel(BaseModel):
    def create_article(self,title, content, uid):
        db = get_db()
        data = db.insert("insert into article value (%s, %s, %s, %s, %s)", None, title, content, None, uid)
        self.db.close()
        return data


    def get_articles(self):
        db = get_db()
        articles = db.query('select * from article order by created_at ASC')
        self.db.close()
        return articles

    def get_hour_articles(self):
        db = get_db()
        articles = db.query('select * from article order by created_at DESC')
        self.db.close()
        return articles

    def get_hot_articles(self):
        db = get_db()
        articles = db.query('select a.*,  (select count(*) from comment where comment.article_id=a.id) as count from article as a order by count DESC')
        self.db.close()
        return articles

    def get_article_id(self, article_id):
        db = get_db()
        article = db.get('select * from article where id=%s',article_id)
        self.db.close()
        return article

    
        
