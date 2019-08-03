import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown_events(event,a_settings,screen,ship,bullets):#按下键盘
    if event.key==pygame.K_RIGHT:
        ship.moving_right = True#向右移动
    if event.key==pygame.K_LEFT:
        ship.moving_left = True#向左移动
    if event.key==pygame.K_UP:
        ship.moving_up = True
    if event.key==pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key==pygame.K_SPACE:
        fire_bullet(a_settings,screen,ship,bullets)

def fire_bullet(a_settings,screen,ship,bullets):
    if len(bullets)<a_settings.bullets_allow:
            new_bullet=Bullet(a_settings,screen,ship)
            bullets.add(new_bullet)
def check_keyup_events(event,ship):#松开键盘
     if event.key == pygame.K_RIGHT:
        ship.moving_right = False
     if event.key == pygame.K_LEFT:
        ship.moving_left = False
     if event.key == pygame.K_UP:
        ship.moving_up = False
     if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(a_settings,screen,stats,play_button,ship,aliens,bullets):
    for event in pygame.event.get():#事件循环
        if event.type == pygame.QUIT:#检测退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,a_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()#函数返回元组，其中包含玩家单机鼠标的x和y坐标
            check_play_button(a_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(a_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #在玩家点击play时候开始游戏
    if play_button.rect.collidepoint(mouse_x,mouse_y):#使用函数判断单机位置是否在play的rect内
        stats.reset_stats()
        stats.game_active=True
        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并让飞船居中
        create_fleet(a_settings,screen,ship,aliens)
        ship.center_ship()
def get_number_aliens_x(a_settings,alien_width):
    #计算每行可容纳多少外星人
    available_space_x = a_settings.screen_width - 2 * alien_width#计算可用于放置外星人的水平空间
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def get_number_rows(a_settings,ship_height,alien_height):
    available_space_y=(a_settings.screen_height -(3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def create_alien(a_settings,screen,aliens,alien_number,row_number):
    alien = Alien(a_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x=alien.x#计算当前外星人的位置
    alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(a_settings,screen,ship,aliens):
    alien=Alien(a_settings,screen)
    number_aliens_x = get_number_aliens_x(a_settings,alien.rect.width)
    number_rows = get_number_rows(a_settings,ship.rect.height,alien.rect.height)
    #alien_width = alien.rect.width#从外星人rect中获取外星人的宽度
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x): #创建外星人 设置X坐标加入当前行
            create_alien(a_settings,screen,aliens,alien_number,row_number)
    #创建一个外星人。并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
def update_screen(a_settings,screen,stats,ship,aliens,bullets,play_button):
        screen.fill(a_settings.bg_color)#重绘屏幕
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        if not stats.game_active:
            play_button.draw_button()
        pygame.display.flip()#刷新屏幕
def update_bullets(a_settings,screen,ship,aliens,bullets):
    """更新子弹位置，删除消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
        #print(len(bullets))#显示当前还有多少子弹,检测完成后删除
    check_bullet_alien_collisions(a_settings,screen,ship,aliens,bullets)
def check_bullet_alien_collisions(a_settings,screen,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)#当发生重叠后返回的字典中添加键-值对
    if len(aliens)==0:
        bullets.empty()#使用empty函数删现有的所有子弹
        create_fleet(a_settings,screen,ship,aliens)
def check_fleet_edges(a_settings,aliens):
    for alien in aliens.sprites():#如果check_edges返回的是true我们需要改变外星人的方向
        if alien.check_edges():
            change_fleet_direction(a_settings,aliens)
            break
def change_fleet_direction(a_settings,aliens):
    #将外星人下移并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y += a_settings.fleet_drop_speed
    a_settings.fleet_direction *= -1
def check_aliens_bottom(a_settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom  >= screen_rect.bottom:
            ship_hit(a_settings,stats,screen,ship,aliens,bullets)
            break


def ship_hit(a_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left -= 1
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()#创建一群新的外星人
        create_fleet(a_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False

def update_aliens(a_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edges(a_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(a_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(a_settings,stats,screen,ship,aliens,bullets)

