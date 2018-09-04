#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.09.01
@author:Marco.Chi
'''
import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    #��Ӧ����������¼�
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    # ÿ��ѭ��ʱ���ػ���Ļ
    screen.fill(ai_settings.bg_color)

    #�ڷɴ��������˺����ػ������ӵ�, ע�����λ�ã�ǰ��˳��
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme();
    # ��������Ƶ���Ļ����
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #�����ƶ��ɴ�
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #����һ���� ������������뵽����bullets��
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right =False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False