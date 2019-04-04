import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats


def run_game():
    """初始化游戏，并创建一个屏幕对象"""
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption("Alien C")

    """创建一个飞船"""
    ship = Ship(ai_settings, screen)

    bullets = Group()

    stats = GameStats(ai_settings)

    """创建外星人"""
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    """开始游戏循环"""
    while True:
        """监视键盘和鼠标"""
        gf.check_events(ai_settings, screen, ship, bullets)  # 用于响应游戏事件
        ship.update()  # 更新飞船状态
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 重绘screen


run_game()
