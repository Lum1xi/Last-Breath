import pygame
from config import screen_width, screen_height, keysBind
from anim import setup_anim

class Player:
    def __init__(self):
        # Позиція та рух
        self.pos = pygame.Vector2(screen_width // 2, screen_height // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.max_speed = 180  # пікселів/секунду
        self.acceleration = 600
        self.friction = 20

        # Анімації
        self.animations = {
            'idle': setup_anim(type="idle"),
            'move': setup_anim(type="move")
        }
        self.state = 'idle'
        self.facing = 'down'
        self.frame_index = 0
        self.animation_time = 0
        self.frame_duration = 100  # мс на кадр

        self.manual_state = None  # Дозволяє примусово задавати стан
        self.input_direction = pygame.Vector2()

        self.hitbox = pygame.Rect(0, 0, 16, 32)
        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox.center = self.pos + pygame.Vector2(0, 8)

    def get_input_direction(self, pressed_keys):
        direction = pygame.Vector2(0, 0)
        # Рух за клавішами
        if any(pressed_keys[k] for k in keysBind["horizontal"]["right"]): direction.x += 1
        if any(pressed_keys[k] for k in keysBind["horizontal"]["left"]): direction.x -= 1
        if any(pressed_keys[k] for k in keysBind["vertical"]["up"]): direction.y -= 1
        if any(pressed_keys[k] for k in keysBind["vertical"]["down"]): direction.y += 1

        # Нормалізація діагонального руху
        if direction.length() > 0:
            direction = direction.normalize()

        return direction

    def update_facing(self, direction):
        if direction.x > 0:
            self.facing = 'right'
        elif direction.x < 0:
            self.facing = 'left'
        elif direction.y > 0:
            self.facing = 'down'
        elif direction.y < 0:
            self.facing = 'up'

    def update_state(self):
        """Оновлює стан на основі вводу або ручних налаштувань"""
        if self.manual_state:
            self.state = self.manual_state
        else:
            self.state = 'move' if self.input_direction.length() > 0 else 'idle'

    def update_animation(self, dt):
        self.animation_time += dt * 1000  # переведення в мілісекунди
        if self.animation_time >= self.frame_duration:
            self.animation_time = 0
            anim_frames = len(self.animations[self.state][self.facing])
            self.frame_index = (self.frame_index + 1) % anim_frames

    def move(self, pressed_keys, dt):
        # Оновлюємо вхід
        self.input_direction = self.get_input_direction(pressed_keys)

        # Фізика руху (не змінює стан автоматично)
        if self.input_direction.length() > 0:
            self.velocity += self.input_direction * self.acceleration * dt
        else:
            self.velocity -= self.velocity * self.friction * dt

        # Обмеження швидкості
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # Оновлюємо позицію
        self.pos += self.velocity * dt

        # Оновлюємо стан
        self.update_state()
        self.update_facing(self.input_direction)
        self.update_hitbox()

    def draw(self, screen, dt):
        self.update_animation(dt)

        try:
            current_anim = self.animations[self.state][self.facing]
        except KeyError:
            current_anim = self.animations['idle']['down']

        frame = current_anim[self.frame_index]
        draw_pos = self.pos - pygame.Vector2(frame.get_width() / 2, frame.get_height() / 2)
        screen.blit(frame, draw_pos)

        # pygame.draw.rect(screen, (255,0,0), self.hitbox, 1)