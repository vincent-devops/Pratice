import sys
import pygame

def check_keydown_events(event, rocket):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动火箭
        # rocket.rect.centerx += 1
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     # 向右移动火箭
            #     # rocket.rect.centerx += 1
            #     rocket.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     rocket.moving_left = True
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     rocket.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     rocket.moving_left = False
            check_keyup_events(event, rocket)


def update_screen(ai_settings, screen, rocket):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 用背景色填充屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制火箭
    rocket.blitme()
    # 刷新屏幕
    pygame.display.flip()