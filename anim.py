import pygame

from config import idle_anim, move_anim


def setup_anim(scale_factor=2, type="idle"):
    if type == "idle":
        config = idle_anim
        sprite_sheet = pygame.image.load(f"assets\\player\\idle\\idle.png").convert_alpha()
    else:
        config = move_anim
        sprite_sheet = pygame.image.load(f"assets\\player\\move\\walk.png").convert_alpha()

    animations = {}
    for anim_name, data in config.items():
        frames = []
        for frame_num in range(data["num_frames"]):
            x = (data["start_col"] + frame_num) * data["frame_width"]
            y = data["row"] * data["frame_height"]
            frame = sprite_sheet.subsurface(pygame.Rect(x, y, data["frame_width"], data["frame_height"]))
            scaled_frame = pygame.transform.scale(frame,
                                                  (int(data["frame_width"] * scale_factor),
                                                   int(data["frame_height"] * scale_factor)))
            frames.append(scaled_frame)
        animations[anim_name] = frames
    return animations