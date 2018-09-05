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
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien, bullets):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重绘所有子弹, 注意代码位置，前后顺序
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme();
    alien.blitme();
    # 让最近绘制的屏幕看见
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right =False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_q:
        sys.exit()

def update_bullets(bullets):
    #更新子弹的位置，并删除消失的子弹
    #更新子弹的位置
    bullets.update()
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    #如果还没有到达限制，就发射一颗子弹
    #创建新的子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)