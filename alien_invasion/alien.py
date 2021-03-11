import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设定其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # # 将外星人放在屏幕上部
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.top


    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

