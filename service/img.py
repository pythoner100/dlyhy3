#coding:utf8

from model.img import ImgModel
from base import BaseService

class ImgService(BaseService):
    def create_img(self):
        yans = self.img_model.create_img()
        
        return yans

    def create_api_img(self, username, password, img):
        yy = self.img_model.create_api_img(username, password, img)
        
        return yy




