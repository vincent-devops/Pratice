import pygame
from settings import Settings
import game_function as gf
from ship import Ship


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("shooting")

    # 飞船
    ship = Ship(screen, ai_settings)

    # 子弹
    bullet = Bu
    # ship_image = pygame.image.load("images/ship.bmp")
    # 翻转图像
    # ship_image = pygame.transform.rotate(ship_image, 270)
    # ship_rect = ship_image.get_rect()
    # screen_rect = screen.get_rect()

    # ship_rect.centery = screen_rect.centery
    # ship_rect.left = screen_rect.left

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        screen.fill(ai_settings.bg_color)
        # 绘制飞船
        # screen.blit(ship_image, ship_rect)
        ship.update()
        ship.blit()
        pygame.display.flip()

run_game()