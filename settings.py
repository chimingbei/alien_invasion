#!/usr/bin/python3
#_*_ coding:utf-8 _*_
'''
Create by 2018.08.29
@author:Marco.Chi
'''
class Settings():
    #存储在《外星人入侵》的所有设置的类
    def __init__(self):
        #初始化设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #飞船的设置
        self.ship_speed_factor = 1.5
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=3
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右，-1表示向左
        self.fleet_direction = 1
