#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.09.08
@author:Marco.Chi
'''

class GameStats():
    #������Ϸ��ͳ����Ϣ
    def __init__(self, ai_settings):
        #��ʼ��ͳ����Ϣ
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #���κ�����²�Ӧ������߷�
        self.high_score = 0
        

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1