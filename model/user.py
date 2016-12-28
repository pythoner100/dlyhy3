#coding:utf8
from base import BaseModel
class UserModel(BaseModel):
    def get_user_info_by_id(self, uid):
        user_info = self.db.get("select username from user where id=%s", uid)
        return user_info
