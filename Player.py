import pygame
from config import screen_width, screen_height, keysBind, item_list
from anim import setup_anim


def get_input_direction(pressed_keys):
    direction = pygame.Vector2(0, 0)
    # Рух за клавішами
    if any(pressed_keys[k] for k in keysBind["horizontal"]["right"]): direction.x += 1
    if any(pressed_keys[k] for k in keysBind["horizontal"]["left"]): direction.x -= 1
    if any(pressed_keys[k] for k in keysBind["vertical"]["up"]): direction.y -= 1
    if any(pressed_keys[k] for k in keysBind["vertical"]["down"]): direction.y += 1

    if direction.length() > 0:
        direction = direction.normalize()

    return direction


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

        self.hitbox = pygame.Rect(0, 0, 32, 32)  # Змініть розмір на 32x32
        self.hitbox.center = self.pos  # Центрування
        self.update_hitbox()

        # Інвентар
        self.inventory = {}

    def remove_inventory(self, item):
        if item in self.inventory:
            if self.inventory[item] > 0:
                self.inventory[item] -= 1
            if self.inventory[item] == 0:
                self.inventory.pop(item)

    def add_inventory(self, item):
        if item in item_list["resources"]:
            if item not in self.inventory:
                self.inventory[item] = 0
            if self.inventory[item] < item_list["resources"][item]["max_stack"]:
                self.inventory[item] += 1

    def get_inventory(self):
        return self.inventory

    def update_hitbox(self):
        self.hitbox.center = self.pos + pygame.Vector2(0, 8)

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
        self.input_direction = get_input_direction(pressed_keys)

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
    def get_pos(self):
        return self.pos