from config import pygame

class Wood:
    def __init__(self):
        self.sprite = pygame.image.load("assets/resources/wood.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (32, 32))
        self.name = "wood"
        self.hitbox = pygame.Rect(0, 0, 16, 16)
    def get_sprite(self):
        return self.sprite