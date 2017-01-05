#coding:utf8

from model.article import ArticleModel
from model.user import UserModel
from base import BaseService

class ArticleService(BaseService):
    def get_articles(self):
        
        articles = self.article_model.get_articles()

        articles = self.add_user_info_to_articles(articles)
      
        return articles

    def get_hour_articles(self):
        articles = self.article_model.get_hour_articles()
        articles = self.add_user_info_to_articles(articles)


        return articles

    def get_hot_articles(self):

        articles = self.article_model.get_hot_articles()
        articles = self.add_user_info_to_articles(articles)

        return articles

    def add_user_info_to_articles(self, articles):
        for article in articles:
            uid = article.uid
            user_info = self.user_model.get_user_info_by_id(uid)
            article['user_info'] = user_info

        return articles

    def create_article(self, title, content, uid):
        data = self.article_model.create_article(title, content, uid)
        
        return data
    
    def get_article_id(self, article_id):
        article = self.article_model.get_article_id(article_id)
        
        return article
    
