# import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from heart import Heart

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # heart = Heart(screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # 更新飞船位置
        ship.update()
        # 重绘屏幕
        gf.update_screen(ai_settings, screen, ship)
        # gf.update_screen(ai_settings, screen, heart)
        # 用背景色填充屏幕
        # screen.fill(ai_settings.bg_color)
        # # 绘制飞船
        # ship.blitme()
        # # 每次循环时都重绘屏幕，以显示新元素
        # pygame.display.flip()

run_game()
