#coding:utf8
import tornado.ioloop
import tornado.web
import os

from handler.index import IndexHandler
from handler.article import ArticleHandler,ApiArticleHandler
from handler.login import LoginHandler,ApiLoginHandler
from handler.register import RegisterHandler,ApiRegisterHandler
from handler.modify import ModifyHandler,ApiModifyHandler
from handler.comment import ApiCommentHandler,ArticleDetailsHandler
from handler.img import ImgHandler, ApiImgHandler

def make_app():
    basedir = os.path.dirname(__file__)
    settings = {
        'debug': True,
        'template_path': os.path.join(basedir, 'template')
    }

    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/article", ArticleHandler),
        (r"/api/article", ApiArticleHandler),
        (r"/login", LoginHandler),
        (r"/api/login", ApiLoginHandler),
        (r"/register", RegisterHandler),
        (r"/api/register", ApiRegisterHandler),
        (r"/modify", ModifyHandler),
        (r"/api/modify", ApiModifyHandler),
        (r"/api/comment", ApiCommentHandler),
        (r"/img", ImgHandler),
        (r"/apiimg", ApiImgHandler),
        (r"/article/(\d+)", ArticleDetailsHandler)
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(5006)
    tornado.ioloop.IOLoop.current().start()


