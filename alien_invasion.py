#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.08.28
@author:Marco.Chi
'''
import sys
import pygame

def run_game():
    #��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
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
        screen.fill(bg_color)
               
        # ��������Ƶ���Ļ����
        pygame.display.flip()

run_game()