#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.08.28
@author:Marco.Chi
'''
import pygame
from pygame.sprite import Sprite

#Sprite ������
class Bullet(Sprite):
    #һ���Էɴ�������ӵ����й������
    def __init__(self, ai_settings, screen, ship):
        #�ڷɴ����ڴ�����һ���ӵ�����
        super(Bullet, self).__init__()
        self.screen = screen

        #��(0, 0) ������һ����ʾ�ӵ����Σ���������ȷ��λ��
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #�洢��С����ʾ���ӵ�λ��
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        #�����ƶ��ӵ�
        #���±�ʾ�ӵ�λ�õ�С��ֵ
        self.y-=self.speed_factor
        #���±�ʾ�ӵ���rect��λ��
        self.rect.y=self.y
    def draw_bullet(self):
        #����Ļ�ϻ����ӵ�
        pygame.draw.rect(self.screen, self.color,self.rect)



