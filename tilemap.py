import pygame
from map import SpawnMap


class Tilemap:
    def __init__(self):
        maps = SpawnMap()
        self.map_data = maps.map_data
        self.tile_size = 16
        self.tileset = maps.tileset
        self.tiles = self.load_tiles()

    def load_tiles(self):
        tiles = {}
        for tile_type, tile_path in self.tileset.items():
            tile_image = pygame.image.load(tile_path).convert_alpha()
            tile_image = pygame.transform.scale(tile_image, (self.tile_size, self.tile_size))
            tiles[tile_type] = tile_image

        return tiles

    def draw(self, screen, camera):
        for y, row in enumerate(self.map_data):
            for x, tile_type in enumerate(row):
                if tile_type in self.tiles:
                    tile_image = self.tiles[tile_type]
                    screen.blit(tile_image, camera.apply(
                        pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)))
