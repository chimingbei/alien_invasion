#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.08.28
@author:Marco.Chi
'''
import sys
import pygame
from settings import Settings

def run_game():
    #��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #���ñ�����ɫ
    bg_color=(230,230,230)

    #��ʼ��Ϸ����ѭ��
    while True:

        #���Ӽ��̺�����¼�
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # ÿ��ѭ��ʱ���ػ���Ļ
        screen.fill(ai_settings.bg_color)
               
        # ��������Ƶ���Ļ����
        pygame.display.flip()

run_game()