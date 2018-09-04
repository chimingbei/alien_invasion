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
def run_game():
    #��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #���ñ�����ɫ
    bg_color=(230,230,230)

    #����һ�ҷɴ�
    ship = Ship(ai_settings,screen)
    bullets=Group()

    #��ʼ��Ϸ����ѭ��
    while True:

        #���Ӽ��̺�����¼�
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship,bullets);
        

run_game()