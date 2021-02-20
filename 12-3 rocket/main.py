import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("rocket")
    # 创建一个火箭
    rocket = Rocket(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(rocket)

        # 根据移动标志调整飞船位置
        rocket.update()
        # # 用背景色填充屏幕
        # screen.fill(ai_settings.bg_color)
        # # 绘制火箭
        # rocket.blitme()
        # # 刷新屏幕
        # pygame.display.flip()
        gf.update_screen(ai_settings, screen, rocket)



run_game()