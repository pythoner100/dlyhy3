#coding:utf8
from util.database import get_db 

class BaseModel(object):
    def __init__(self):
        self.db = get_db()
