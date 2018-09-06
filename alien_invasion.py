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
    #��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #���ñ�����ɫ
    bg_color=(230,230,230)

    #����һ�ҷɴ���һ���ӵ������һ�������˱���
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens = Group()
    #����������Ⱥ
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #��ʼ��Ϸ����ѭ��
    while True:

        #���Ӽ��̺�����¼�
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        gf.update_bullets(bullets);
        gf.update_alien(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets);
        

run_game()