import pygame

pygame.init()

keysBind = {
    "horizontal": {
        "left": [pygame.K_a, pygame.K_LEFT],
        "right": [pygame.K_d, pygame.K_RIGHT]
    },
    "vertical": {
        "up": [pygame.K_w, pygame.K_UP],
        "down": [pygame.K_s, pygame.K_DOWN]
    }
}

idle_anim = {
    "down": {"row": 0, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "up": {"row": 1, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "down_left": {"row": 2, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "down_right": {"row": 3, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "up_right": {"row": 4, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "up_left": {"row": 5, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},

}

move_anim = {
    "down": {"row": 0, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "up": {"row": 1, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "down_left": {"row": 2, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "down_right": {"row": 3, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "up_right": {"row": 4, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},
    "up_left": {"row": 5, "start_col": 0, "num_frames": 8, "frame_width": 48, "frame_height": 64},

}
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
x, y = screen_width / 2, screen_height / 2
speed_x, speed_y = 0, 0
FPSLimit = 60

frame_time = pygame.time.Clock()
