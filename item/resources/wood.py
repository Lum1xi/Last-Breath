import pygame

class Wood(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.Vector2(x, y)
        self.sprite = pygame.image.load("assets/resources/wood.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (32, 32))
        self.rect = self.sprite.get_rect(center=(x, y))
        self.hitbox = self.rect.copy()  # Хітбокс = копія rect

    def update(self):
        self.rect.center = (round(self.pos.x), round(self.pos.y))  # Округлення координат
        self.hitbox.center = self.rect.center  # Хітбокс точно по центру спрайту

    def draw_wood(self, screen, camera):
        if self.sprite is not None:
            # Draw sprite and hitbox with camera offset
            screen.blit(self.sprite, camera.apply(self.rect))
            # pygame.draw.rect(screen, (255, 0, 0), camera.apply(self.hitbox), 1)