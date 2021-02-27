class Settings():
    '''存储game用到的所有设置'''
    def __init__(self):
        """初始化游戏的所有设置"""
        # 屏幕设置
        self.screen_width = 700
        self.screen_height = 500
        self.bg_color = (135, 206, 235)
        # 飞船速度设置
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60,60,60



