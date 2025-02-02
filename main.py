import pygame
from Player import Player
from config import screen_width, screen_height, screen, frame_time
from setup import setup  # Прибрано зайві імпорти

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

    # Викликаємо move ВЗАГАЛІ ЗАВЖДИ для коректного тертя
    player.move(keys, dt)

    # Оновлюємо анімацію та позицію (всередині класу Player)
    player.draw(screen, dt)

    # Відображення
    pygame.display.update()
    screen.fill((0, 0, 0))  # Очищення екрану після відмальовки

pygame.quit()