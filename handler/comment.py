#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from model.comment import CommentModel
from model.article import ArticleModel
from model.user import UserModel

class ApiCommentHandler(tornado.web.RequestHandler):
    def post(self):
        article_id = self.get_argument('article_id')
        content = self.get_argument('content')
        uid = self.get_cookie('uid')

        comment_model = CommentModel()
        data = comment_model.create_comment(content, article_id, uid)
        self.redirect('/')
        
        
class ArticleDetailsHandler(tornado.web.RequestHandler):
    def get(self,article_id):
        db = get_db()
        article_model = ArticleModel()
        article = article_model.get_article_id(article_id)
        user = db.get('select * from user where id=%s', article.uid)
        comment_model = CommentModel()
        comments = comment_model.query_comment_article_id(article_id)
        for comment in comments:
            uid = comment.uid
            user_model = UserModel()
            user_info = user_model.get_user_info_by_uid(uid)
            comment['user_info'] = user_info

        db.close()
        self.render('comment.html',comments=comments,article=article, user=user,)

                                                                                        
                                                                                              
