#coding:utf8
import torndb

class BaseModel(object):
    def __init__(self, *args, **kwargs):
        self.db = torndb.Connection(host = "localhost", database = "hy3", user = "root", password = "11111111")
        
