import sys
import pygame


def run_game():
    # 初始化所有导入的pygame模块
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("blank")

    while True:
        bg_color = (230, 230, 230)
        screen.fill(bg_color)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


run_game()
