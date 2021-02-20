import pygame

class Rocket():
    def __init__(self, ai_settings, screen):
        """初始化火箭并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将火箭放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.centerx += self.ai_settings.ship_speed_factor
        # 添加了一个if代码块而不是elif代码块，这样如果玩家同时按下了左右箭头键，将先增大飞船的rect.centerx值，再降低这个值，即飞船的位置保持不变。如果使用一个elif代码块来处理向左移动的情况，右箭头键将始终处于优先地位。从向左移动切换到向右移动时，玩家可能同时按住左右箭头键，在这种情况下，前面的做法让移动更准确。
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.centerx -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top >0:
            # self.rect.centery -= 1
            self.centery -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # self.rect.centery += 1
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)
