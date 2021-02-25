import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""
    def __init__(self, screen, ai_settings, ship):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 将子弹移到正确的位置
        self.rect.centery = ship.rect.centery
        self.rect.bottom = ship.rect.bottom
        self.rect.color = ai_settings.bullet_height

    def update(self):
        # 更新子弹位置
        pass

    def blit(self):
        # 重绘子弹
        self.screen.blit(self.rect)


