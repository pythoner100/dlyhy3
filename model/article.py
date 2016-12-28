#coding:utf8
#from base import BaseModel
import torndb
from user import UserModel

class ArticleModel(BaseModel):
    def get_all_articles(self):
        articles = self.db.query('select * from article')
        user_model = UserModel()

        for article in articles:
            uid = article.uid
            user_info =user_model.get_user_info_by_id(uid)
            article["user_info"] = user_info
        self.db.close()
        
        return articles

    def get_all_articles_order_by_comment_count(self):
        
        articles = self.db.query("select * from article order by created_at DESC")
        user_model = UserModel()
        #comment_model =commentModel()
        for article in articles:
            uid = article.uid
            user_info = user_model.get_user_info_by_id(uid)
            article["user_info"] = user_info
        self.db.close()
        
        return articles

    def get_articles_order_by_time(self):
        articles = self.db.query(
            "select a.*, (select count(*) from comment where comment.article_id=a.id) as count from article as a  order by count desc")
        user_model = UserModel()
        #comment_model = commentModel()
       
        for article in articles:
            uid = article.uid
            user_info = user_model.get_user_info_by_id(uid)
            
            article["user_info"] = user_info
        self.db.close()
 
        return articles

