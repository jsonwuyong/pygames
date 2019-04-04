import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):# 使用精灵
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx   # 从飞机的中央位置射出
        self.rect.top = ship.rect.top  # 从飞机的顶部射出

        # 存储用浮点数表示的子弹位置，因为子弹只在y轴上运动，所以不需要x坐标
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color   # 子弹颜色
        self.speed_factor = ai_settings.bullet_speed_factor   # 子弹速度

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的浮点数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):

        pygame.draw.rect(self.screen,self.color,self.rect)
