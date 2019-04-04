class Settings():
    """存储设置的地方"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_with = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5  # 飞船的移动速度
        # 飞船的设置
        self.ship_limt = 3  # 3条命

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 221, 42, 42
        # 表示窗口中最多允许存在的子弹数，当然你也可以将其去掉
        self.bullets_allowed = 50

        # 以什么样的速度去加快游戏节奏
        self.speedup_scale = 1.2


        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10  # 外星人竖直移动速度
        self.fleet_direction = -1

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
