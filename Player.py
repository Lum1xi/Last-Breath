from config import screen_width, screen_height, keysBind, idle_anim, move_anim
from anim import setup_anim
import pygame
from math import sqrt


class Player:
    def __init__(self):
        # Позиція та рух
        self.pos = pygame.Vector2(screen_width // 2, screen_height // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.max_speed = 180  # пікселів/секунду
        self.acceleration = 600
        self.friction = 600

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

        # Хітбокс
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
        if direction.length() == 0:
            return

        angles = {
            'up_right': 0,
            'down_right': 45,
            'down': 90,
            'down_left': 135,
            'down_left': 180,
            'up_left': 225,
            'up': 270,
            'up_right': 315
        }

        angle = direction.angle_to(pygame.Vector2(0, -1))  # 0° = вгору
        closest = min(angles.values(), key=lambda x: abs(x - angle))
        self.facing = [k for k, v in angles.items() if v == closest][0]

    def update_state(self):
        self.state = 'move' if self.velocity.length() > 10 else 'idle'

    def update_animation(self, dt):
        self.animation_time += dt * 1000  # переведення в мілісекунди
        if self.animation_time >= self.frame_duration:
            self.animation_time = 0
            anim_frames = len(self.animations[self.state][self.facing])
            self.frame_index = (self.frame_index + 1) % anim_frames

    def move(self, pressed_keys, dt):
        # Вхідні дані гравця
        input_dir = self.get_input_direction(pressed_keys)

        # Оновлення напрямку
        self.update_facing(input_dir if input_dir.length() > 0 else self.velocity)

        # Фізика руху
        if input_dir.length() > 0:
            self.velocity += input_dir * self.acceleration * dt
        else:
            self.velocity -= self.velocity * self.friction * dt

        # Обмеження швидкості
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # Оновлення позиції
        self.pos += self.velocity * dt
        self.pos.x = pygame.math.clamp(self.pos.x, 0, screen_width)
        self.pos.y = pygame.math.clamp(self.pos.y, 0, screen_height)

        self.update_state()
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

        # Відладка хітбоксу (опційно)
        # pygame.draw.rect(screen, (255,0,0), self.hitbox, 1)