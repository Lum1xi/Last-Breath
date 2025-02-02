import pygame
from config import screen_width, screen_height


# Camera.py
class Camera:
    def __init__(self):
        self.offset = pygame.Vector2(0, 0)

    def update(self, target_pos):
        # Центруємо камеру на гравцю
        self.offset.x = target_pos.x - screen_width // 2
        self.offset.y = target_pos.y - screen_height // 2

    def apply(self, rect):
        # Зміщуємо rect на офсет камери (і округлюємо)
        return rect.move(-int(self.offset.x), -int(self.offset.y))
