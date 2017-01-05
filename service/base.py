#coding:utf8
from model.article import ArticleModel
from model.user import UserModel
from model.comment import CommentModel
from model.img import ImgModel

class BaseService(object):
    def __init__(self):
        self.article_model = ArticleModel()
        self.user_model = UserModel()
        self.comment_model = CommentModel()
        self.img_model = ImgModel()
