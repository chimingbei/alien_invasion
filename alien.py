#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.09.25
@author:Marco.Chi
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类

    def __init__(self, ai_settings, screen):
        #初始化外星人并设置其起始位置
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像
        self.image = pygame.image.load(r'G:\file\git_project\alien_invasion\images\alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width;
        self.rect.y = self.rect.height

        #存储外星人的位置 
        self.x = float(self.rect.x)

    def blitme(self):
        #在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
