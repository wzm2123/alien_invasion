# 作者：王子明
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from picture import Picture
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    #游戏名字
    pygame.display.set_caption("怪兽入侵 (王子明制作)")
    #  创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    back_picture = Picture(ai_settings ,screen)
    #  创建 Play 按钮
    play_button = Button(ai_settings, screen,"play" )
    #创建一艘飞船
    ship = Ship(ai_settings ,screen)
    bullets = Group()
    aliens = Group()
    #alien = Alien(ai_settings,screen)
    #  创建外星人群
    gf.create_fleet(ai_settings, screen,ship,aliens)

    #开始游戏循环


    while True:

        gf.check_events(ai_settings, screen, stats, sb,play_button, ship,
                            aliens, bullets)
        if stats.game_active:
            ship.update()

            bullets.update()

            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)




            gf.update_aliens(ai_settings,screen,stats,sb,ship, aliens,bullets)

        gf.update_screen(ai_settings,screen,back_picture ,stats,sb,ship,aliens,bullets,play_button )
run_game()








