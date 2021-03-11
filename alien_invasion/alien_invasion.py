# import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
# from heart import Heart

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # heart = Heart(screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # 更新飞船位置
        ship.update()
        # 更新子弹的位置
        gf.update_bullets(bullets)
        # print(len(bullets))
        # 使用更新后的位置来绘制新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)
        # gf.update_screen(ai_settings, screen, heart)
        # 用背景色填充屏幕
        # screen.fill(ai_settings.bg_color)
        # # 绘制飞船
        # ship.blitme()
        # # 每次循环时都重绘屏幕，以显示新元素
        # pygame.display.flip()

run_game()
