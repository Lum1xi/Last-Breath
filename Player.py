import pygame

from config import screen_width, screen_height, keysBind

class Player:
    def __init__(self):
        self.x, self.y = int(screen_width / 2), int(screen_height / 2)
        self.speed_x, self.speed_y = 0, 0
        self.max_speed = 2
        self.acceleration = 0.2
        self.friction = 0.1

    def stop_move(self, pressed_keys):
        if not pressed_keys[pygame.K_w] and not pressed_keys[pygame.K_s]:
            if abs(self.speed_y) > 0:
                self.speed_y -= self.friction * (1 if self.speed_y > 0 else -1)
                if abs(self.speed_y) < self.friction:
                    self.speed_y = 0

        if not pressed_keys[pygame.K_a] and not pressed_keys[pygame.K_d]:
            if abs(self.speed_x) > 0:
                self.speed_x -= self.friction * (1 if self.speed_x > 0 else -1)
                if abs(self.speed_x) < self.friction:
                    self.speed_x = 0

    def test_max_speed(self):
        self.speed_x = max(-self.max_speed, min(self.speed_x, self.max_speed))
        self.speed_y = max(-self.max_speed, min(self.speed_y, self.max_speed))

    def move(self, pressed_keys):
        if any(pressed_keys[key] for key in keysBind["horizontal"]["right"]):
            self.speed_x += self.acceleration
        if any(pressed_keys[key] for key in keysBind["horizontal"]["left"]):
            self.speed_x -= self.acceleration
        if any(pressed_keys[key] for key in keysBind["vertical"]["up"]):
            self.speed_y -= self.acceleration
        if any(pressed_keys[key] for key in keysBind["vertical"]["down"]):
            self.speed_y += self.acceleration
        self.test_max_speed()
        return self.speed_x, self.speed_y

