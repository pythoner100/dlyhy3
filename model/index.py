from util.database import get_db

def get_articles():
   db = get_db()
   articles = db.query('select * from article order by created_at ASC')
   for article in articles:
       uid = article.uid
       user_info = db.get('select id,username from user where id=%s',uid)
       article['user_info'] = user_info
   db.close()
   return articles

def get_hour_articles():
   db = get_db()
   articles = db.query('select * from article order by created_at DESC')
   for article in articles:
       uid = article.uid
       user_info = db.get('select id,username from user where id=%s',uid)
       article['user_info'] = user_info
   db.close()
   return articles

def get_hot_articles():
   db = get_db()
   articles = db.query('select a.*,  (select count(*) from comment where comment.article_id=a.id) as count from article as a order by count DESC')
   for article in articles:
       uid = article.id
       user_info = db.get('select * from user where id=%s',uid)
       article['user_info'] = user_info
   db.close()
   return articles

