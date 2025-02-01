import pygame
from Player import Player
from config import screen_width, screen_height, screen, frame_time, FPSLimit, x, y, keysBind
from setup import verticalBind, horizontalBind, setup

setup()
player = Player()

while True:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if any(keys[key] for key in verticalBind + horizontalBind):
        player.move(keys)
    else:
        player.stop_move(keys)
    if any(keys[key] for key in verticalBind):
        player.stop_move(keys)
    if any(keys[key] for key in horizontalBind):
        player.stop_move(keys)

    x, y = x + player.speed_x, y + player.speed_y
    x = max(0, min(x, screen_width - 50))
    y = max(0, min(y, screen_height - 50))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50), 0)

    pygame.display.update()
    frame_time.tick(FPSLimit)
