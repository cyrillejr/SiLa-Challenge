import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self, world_width, world_height):
        self.offset = pygame.Vector2(0, 0)
        self.world_width = world_width
        self.world_height = world_height

    def follow(self, target):
        x = target.rect.centerx - SCREEN_WIDTH // 2
        y = target.rect.centery - SCREEN_HEIGHT // 2
        
        # Garder la caméra dans les limites du monde
        x = max(0, min(x, self.world_width - SCREEN_WIDTH))
        y = max(0, min(y, self.world_height - SCREEN_HEIGHT))
        self.offset = pygame.Vector2(x, y)

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)