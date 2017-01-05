#coding:utf8
from util.database import get_db
from base import BaseModel

class CommentModel(BaseModel):
    def create_comment(self, content, article_id, uid):
        self.db = get_db()
        data = self.db.insert('insert into comment values (%s, %s, %s, %s, %s)', None, content, None, article_id, uid)
        self.db.close()

        return data
     
    def query_comment_article_id(self, article_id):
        self.db = get_db()
        comments = self.db.query("select * from comment where article_id=%s",article_id)
        self.db.close()
        
        return comments
