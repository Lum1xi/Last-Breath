import pygame

pygame.init()

keysBind = {
    "vertical": {
        "up": [pygame.K_UP, pygame.K_w],
        "down": [pygame.K_DOWN, pygame.K_s]
    },
    "horizontal": {
        "right": [pygame.K_RIGHT, pygame.K_d],
        "left": [pygame.K_LEFT, pygame.K_a]
    }
}


info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.RESIZABLE)
x, y = screen_width / 2, screen_height / 2
speed_x, speed_y = 0, 0
FPSLimit = 60
frame_time = pygame.time.Clock()
