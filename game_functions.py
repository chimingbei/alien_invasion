#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.09.01
@author:Marco.Chi
'''
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    #��Ӧ����������¼�
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    # ÿ��ѭ��ʱ���ػ���Ļ
    screen.fill(ai_settings.bg_color)

    #�ڷɴ��������˺����ػ������ӵ�, ע�����λ�ã�ǰ��˳��
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme();
    aliens.draw(screen)
    # ��������Ƶ���Ļ����
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #�����ƶ��ɴ�
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
    #�����ӵ���λ�ã���ɾ����ʧ���ӵ�
    #�����ӵ���λ��
    bullets.update()
    #ɾ����ʧ���ӵ�
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    #�����û�е������ƣ��ͷ���һ���ӵ�
    #�����µ��ӵ�����������뵽����bullets��
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def create_fleet(ai_settings, screen, ship, aliens):
    #����������Ⱥ
    #����һ�������ˣ�������һ�п����ɶ��ٸ�������
    #�����˼��Ϊ�����˵Ŀ��
    alien = Alien(ai_settings, screen)
    alien_width=alien.rect.width;
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #������һ��������Ⱥ
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    #����ÿ�п����ɶ��ٸ�������
    available_space_x=ai_settings.screen_width - 2 * alien_width
    number_aliens_x=int(available_space_x / (2 * alien_width))
    return number_aliens_x
   
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #����һ�������˲�������뵽��ǰ��
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x=alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    #������Ļ�����ɶ�����������
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def update_alien(ai_settings, aliens):
    #����Ƿ���������λ����Ļ��Ե�� ��������Ⱥ�����˵�λ��
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    #�������˵����Եʱ��ȡ��Ӧ�Ĵ�ʩ
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break;
 
def change_fleet_direction(ai_settings, aliens):
    #����Ⱥ���������ƣ����ı����ǵķ���
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1