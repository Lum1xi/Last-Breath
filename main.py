import pygame
from Player import Player
from config import screen, frame_time
from setup import setup

# Ініціалізація
pygame.init()
setup()
player = Player()

# Головний цикл гри
running = True
while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлення стану гри
    dt = frame_time.tick(60) / 1000  # Обчислюємо dt перед оновленнями
    keys = pygame.key.get_pressed()

    # Викликаємо move завжди для коректного тертя
    player.move(keys, dt)

    # Відображення
    screen.fill((0, 0, 0))  # Очищення екрану перед відмальовкою
    player.draw(screen, dt)
    pygame.display.update()

pygame.quit()