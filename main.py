import pygame

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.RESIZABLE)
x, y = screen_width / 2, screen_height / 2
speed_x, speed_y = 0, 0
FPSLimit = 60
frame_time = pygame.time.Clock()


class Player:
    def __init__(self):
        self.x, self.y = int(screen_width / 2), int(screen_height / 2)
        self.speed_x, self.speed_y = 0, 0
        self.max_speed = 5
        self.acceleration = .2
        self.friction = .3

    def test_max_speed(self):
        if self.speed_x > self.max_speed:
            self.speed_x = self.max_speed
        if self.speed_y > self.max_speed:
            self.speed_y = self.max_speed
        if self.speed_x < -self.max_speed:
            self.speed_x = -self.max_speed
        if self.speed_y < -self.max_speed:
            self.speed_y = -self.max_speed

    def move(self, pressed_keys):
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.speed_x += self.acceleration
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.speed_x -= self.acceleration
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.speed_y -= self.acceleration
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.speed_y += self.acceleration
        return self.speed_x, self.speed_y


player = Player()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    x, y = x + player.speed_x, y + player.speed_y
    x = max(0, min(x, screen_width - 50))
    y = max(0, min(y, screen_height - 50))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50), 0)

    pygame.display.flip()

    frame_time.tick(FPSLimit)
