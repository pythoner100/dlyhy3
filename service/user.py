#coding:utf8

from model.user import UserModel
from base import BaseService

class UserService(BaseService):
    def get_user_register(self, username, password):
        data = self.user_model.get_user_register(username, password)
         
        return data

    def get_user_info_by_uid(self, uid):
        user_info = self.user_model.get_user_info_by_uid(uid)
         
        return user_info

    def get_user_by_username(self, username):
        data = self.user_model.get_user_by_username(username)
        
        return data

    def get_user_by_password(self, username, password):
        data3 = self.user_model.get_user_by_password(username, password)

        return data3

    def update_user_by_username(self, username):
        data2 = self.user_model.update_user_by_username(username)

        return data2

    def get_user_modify_data(self, username, password):
        data = self.user_model.get_user_modify_data(username, password)

        return data

    def update_user_modify_data2(self, password1, username):
        data2 = self.user_model.update_user_modify_data2(password1, username)
        
        return data2

    def get_user_by_id(self, article_uid):
        user = self.user_model.get_user_by_id(article_uid)

        return user

    def get_user_article_by_uid(self, uid):
        user = self.user_model.get_user_article_by_uid(uid)
      
        return user
  
        




