#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.08.29
@author:Marco.Chi
'''
class Settings():
    #�洢�ڡ����������֡����������õ���
    def __init__(self):
        #��ʼ������
        #��Ļ����
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #�ɴ�������
        self.ship_speed_factor = 1.5
        #�ӵ�����
        self.bullet_speed_factor = 1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=3
