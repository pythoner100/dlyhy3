#coding:utf8
import tornado.web
import torndb


class ApiCommentHandler(tornado.web.RequestHandler):
    def post(self):
        article_id = self.get_argument('article_id')
        content = self.get_argument('content')
        uid = self.get_cookie('uid')

        db = torndb.Connection(host='localhost', database='hy3', user='root', password='11111111')
        data = db.insert('insert into comment values (%s, %s, %s, %s, %s)', None, content, None, article_id, uid)
        db.close()

        self.redirect('/')
        
class ArticleDetailsHandler(tornado.web.RequestHandler):
    def get(self,article_id):
        db = torndb.Connection(host = "localhost", database = "hy3", user = "root", password = "11111111")
        article = db.get('select * from article where id=%s',article_id)
        user = db.get('select * from user where id=%s', article.uid)
        comments = db.query("select * from comment where article_id=%s",article_id)
        for comment in comments:
            uid = comment.uid
            user_info = db.get('select * from user where id=%s',uid)
            comment['user_info'] = user_info

        db.close()
        self.render('comment.html',comments=comments,article=article, user=user)

                                                                                        
                                                                                              
