import pygame

class Ship():
    """飞船类"""
    # 初始化飞船，并设定位置
    def __init__(self, screen):
        self.screen = screen
        self.befor_turn_image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.befor_turn_image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设定飞船位置
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # 设定移动属性
        self.moving_up = False
        self.moving_down = False


    def update(self):
        # 更新飞船位置
        if self.moving_up and self.rect.centery > self.screen_rect.top:
            self.rect.centery -= 1
        elif self.moving_down:
            self.rect.centery += 1

    def blit(self):
        # 重绘飞船
        self.screen.blit(self.image, self.rect)

