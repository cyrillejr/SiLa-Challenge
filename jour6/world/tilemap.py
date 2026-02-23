import json, pygame
from settings import TILE_SIZE, GRAY

class World:
    def __init__(self, filename):
        self.platforms = []
        with open(filename, 'r') as f:
            self.data = json.load(f)
        
        self.width = len(self.data["map"][0]) * TILE_SIZE
        self.height = len(self.data["map"]) * TILE_SIZE
        
        for y, row in enumerate(self.data["map"]):
            for x, cell in enumerate(row):
                if cell == "1":
                    self.platforms.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def draw(self, screen, camera):
        for tile in self.platforms:
            pygame.draw.rect(screen, GRAY, camera.apply(tile))