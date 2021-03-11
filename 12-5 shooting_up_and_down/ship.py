import pygame

class Ship():
    """飞船类"""
    # 初始化飞船，并设定位置
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.befor_turn_image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.befor_turn_image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设定飞船位置
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # 在飞船的属性centery中存储小数值
        self.centery = float(self.rect.centery)

        # 设定移动属性
        self.moving_up = False
        self.moving_down = False


    def update(self):
        # 更新飞船位置
        if self.moving_up and self.rect.centery > self.screen_rect.top:
            # self.rect.centery -= 1
            self.centery -= self.ai_settings.ship_speed_factor
        elif self.moving_down and  self.rect.centery < self.ai_settings.screen_height:
            # print(self.rect.centery)
            # self.rect.centery += 1
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centery = self.centery

    def blitme(self):
        # 重绘飞船
        self.screen.blit(self.image, self.rect)

