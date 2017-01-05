#coding:utf8
import tornado.web
from service.article import ArticleService
from service.user import UserService
from service.comment import CommentService
from service.img import ImgService

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        self.article_srv = ArticleService()
        self.user_srv = UserService()
        self.comment_srv = CommentService()
        self.img_srv = ImgService()




