#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.09.25
@author:Marco.Chi
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #��ʾ���������˵���

    def __init__(self, ai_settings, screen):
        #��ʼ�������˲���������ʼλ��
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #����������ͼ��
        self.image = pygame.image.load(r'G:\file\git_project\alien_invasion\images\alien.bmp')
        self.rect = self.image.get_rect()

        #ÿ�����������������Ļ�����ϽǸ���
        self.rect.x = self.rect.width;
        self.rect.y = self.rect.height

        #�洢�����˵�λ�� 
        self.x = float(self.rect.x)

    def blitme(self):
        #��ָ��λ�û���������
        self.screen.blit(self.image, self.rect)
    def update(self):
        #�����ƶ�������
        self.x +=(self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        #���������λ����Ļ�ı�Ե���ͷ���True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
