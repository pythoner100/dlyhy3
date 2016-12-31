#coding:utf8
from util.database import get_db

class CommentModel(object):
    def create_comment(self, content, article_id, uid):
        db = get_db()
        data = db.insert('insert into comment values (%s, %s, %s, %s, %s)', None, content, None, article_id, uid)
        db.close()

        return data
     
    def query_comment_article_id(self, article_id):
        db = get_db()
        comments = db.query("select * from comment where article_id=%s",article_id)
        db.close()
        
        return comments
