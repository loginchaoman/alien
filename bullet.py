import pygame
from pygame.sprite import  Sprite
class Bullet(Sprite):
    def __init__(self,a_setting,screen,ship):
        super(Bullet,self).__init__()#继承Sprite类
        self.screen=screen
        #在00处创建一个表示子弹的矩形，在设置正确的位置
        self.rect=pygame.Rect(0,0,a_setting.bullet_width,a_setting.bullet_height)
        #子弹不基于图像，创建空白的矩形提供矩形左上方的坐标以及初始高度和宽度
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)#将子弹的Y坐标存储为小数值，便于调节子弹的速度
        self.color=a_setting.bullet_color
        self.speed_factor=a_setting.bullet_speed_factor
    def update(self):
        self.y-=self.speed_factor#控制子弹向上
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
