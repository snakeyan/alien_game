#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/10

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    
    bullets = Group()
    
    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        
        #删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        #print(len(bullets))
        
        gf.update_screen(ai_settings,screen,ship,bullets)
        
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()