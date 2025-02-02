import pygame
from Player import Player
from config import screen, frame_time
from setup import setup
from dev_menu import show_fps
from item.resources.wood import Wood
from Camera import Camera
from tilemap import Tilemap

# Initialization
pygame.init()
setup()
player = Player()
camera = Camera()

# Create wood object before game loop
wood = Wood(x=100, y=200)

running = True
tilemap = Tilemap()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game state update
    dt = frame_time.tick(60) / 1000
    keys = pygame.key.get_pressed()

    player.move(keys, dt)

    # Update camera
    camera.update(player.pos)

    # Clear screen
    screen.fill((0, 0, 0))

    # Display FPS
    show_fps(screen, frame_time, pygame.font.SysFont("Comic Sans MS", 36))

    # Draw tilemap
    tilemap.draw(screen, camera)

    # Draw wood and check collision
    if wood and wood.sprite is not None:
        wood.update()  # Update wood position and hitbox
        wood.draw_wood(screen, camera)
        if wood.hitbox.colliderect(player.hitbox):
            print("Collision! Wood collected.")
            player.add_inventory("wood")
            wood = None

    # Debug output
    print(f"Player: world position {player.pos}, hitbox {player.hitbox}")
    if wood:
        print(f"Wood: world position {wood.pos}, hitbox {wood.hitbox}")
    # pygame.draw.rect(screen, (0, 255, 0), player.hitbox, 1)
    if wood:
        # pygame.draw.rect(screen, (255, 0, 0), wood.hitbox, 1)
        pass
    player.draw(screen, dt)
    pygame.display.update()

pygame.quit()