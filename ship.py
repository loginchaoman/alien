import pygame
class Ship():
    def __init__(self,a_settings,screen):
        self.screen=screen
        self.a_settings=a_settings
        #加载飞船图像并获取它外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #j将飞船放在底部
        self.rect.centerx = self.screen_rect.centerx#x中央
        self.rect.centery=self.screen_rect.bottom#y
        #self.rect.bottom = self.screen_rect.bottom#底部
        #飞船的属性center中存贮数值
        self.center=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.a_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.a_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.a_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.a_settings.ship_speed_factor
        #根据center更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.centery
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.center=self.screen_rect.centerx
        self.centery=self.screen_rect.bottom#y