#coding:utf8
import tornado.web
import torndb
from util.database import get_db
from base import BaseHandler

class ApiCommentHandler(BaseHandler):
    def post(self):

        uid = self.get_cookie('uid')
        if uid is None:
           self.write('您还没登录')
           return

        article_id = self.get_argument('article_id')
        content = self.get_argument('content')
        uid = self.get_cookie('uid')
        data = self.comment_srv.create_comment(content, article_id, uid)
        self.redirect('/')
        
        
class ArticleDetailsHandler(BaseHandler):
    def get(self,article_id):
        article = self.article_srv.get_article_id(article_id)
        user = self.user_srv.get_user_by_id(article.uid)
        comments = self.comment_srv.query_comment_article_id(article_id)
        for comment in comments:
            uid = comment.uid
            user_info = self.user_srv.get_user_info_by_uid(uid)
            comment['user_info'] = user_info

        self.render('comment.html',comments=comments,article=article, user=user,)

                                                                                        
                                                                                              
