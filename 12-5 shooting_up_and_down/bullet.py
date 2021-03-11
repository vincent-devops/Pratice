import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 将子弹移到正确的位置
        self.rect.centery = ship.rect.centery
        self.color = ai_settings.bullet_color

    def update(self):
        # 更新子弹位置
        self.rect.centerx += 1

    def draw_bullet(self):
        # 重绘子弹
        pygame.draw.rect(self.screen, self.color, self.rect)


