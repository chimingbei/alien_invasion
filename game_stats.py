#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.09.08
@author:Marco.Chi
'''

class GameStats():
    #跟踪游戏的统计信息
    def __init__(self, ai_settings):
        #初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit