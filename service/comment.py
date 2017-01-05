#coding:utf8

from model.comment import CommentModel
from base import BaseService

class CommentService(BaseService):
    def create_comment(self, content, article_id, uid):
        data = self.comment_model.create_comment(content, article_id, uid)
        
        return data

    def query_comment_article_id(self, article_id):
        comments = self.comment_model.query_comment_article_id(article_id)

        return comments









