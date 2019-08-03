import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import  GameStats
from Button import Button
def run_game():
    #初始化游戏创建一个对象
    pygame.init()
    a_settings=Settings()
    screen=pygame.display.set_mode((a_settings.screen_width,a_settings.screen_height))#使用元组指定屏幕的尺寸。
    stats=GameStats(a_settings)
    pygame.display.set_caption(" Alien Invasion")
    play_button = Button(a_settings,screen,"PLAY")
    ship = Ship(a_settings,screen)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(a_settings,screen,ship,aliens)
    alien=Alien(a_settings,screen)
    bg_color=a_settings.bg_color
    #bg_color = (240,230,230)#设置背景色
    while True:

        gf.check_events(a_settings,screen,stats,play_button,ship,aliens,bullets)#监视鼠标和键盘事件
        if stats.game_active:
            ship.update()#更新飞船的位置
            gf.update_bullets(a_settings,screen,ship,aliens,bullets)
            gf.update_aliens(a_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(a_settings,screen,stats,ship,aliens,bullets,play_button)


run_game()