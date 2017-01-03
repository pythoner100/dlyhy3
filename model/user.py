#coding:utf8
from util.database import get_db


class UserModel(object):
    def get_user_info_by_id(self, uid):
        db = get_db()
        data = db.get('select id, username from user where id=%s', uid)
        db.close()

        return data

    def get_user_register(self, username, password):
        db = get_db()
        data = db.insert("insert into user value(%s, %s, %s, %s, %s)", None, username, password, None, None)
        db.close()
        
        return data
    
    def get_user_info_by_uid(self, uid):
        db = get_db()
        user = db.get('select * from user where id=%s', uid)
        db.close()
       
        return user

    def get_user_by_username(self, username):
        db = get_db()
        data = db.get("select last_login_at from user where username = %s", username)    
        db.close()
        
        return data

    def update_user_by_username(self, username):
        db = get_db()
        data2 = db.update("update user set last_login_at = NULL where username = %s", username)
        db.close()
        
        return data2

    def get_user_by_password(self, username, password):
        db = get_db()
        data3 = db.get("select id from user where username=%s and password = %s",username, password)
        db.close()
       
        return data3

    def get_user_modify_data(self, username, password):
        db = get_db()
        data = db.get("select id from user where username = %s and password = %s", username,password)
        db.close()
        
        return data

    def update_user_modify_data2(self, password1, username):
        db = get_db()
        data2 = db.update("update user set password=%s where username = %s", password1, username)
        db.close()
        
        return data2

    
    def get_user_by_id(self, article_uid):
        db = get_db()
        user = db.get('select * from user where id=%s', article_uid)
        db.close()

        return user

  
    def get_user_article_by_uid(self, uid):
        db = get_db()
        user = db.get('select id from user where id=%s', uid)
        db.close()
       
        return user
       
 
