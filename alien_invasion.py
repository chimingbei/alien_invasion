#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.08.28
@author:Marco.Chi
'''
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color=(230,230,230)

    #创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        gf.update_bullets(bullets);
        gf.update_alien(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets);
        

run_game()