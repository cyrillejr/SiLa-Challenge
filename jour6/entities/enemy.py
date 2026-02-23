import pygame
from .base import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32)
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0)) 
        self.speed = 2

    def update(self, player, platforms):
        dist = player.rect.centerx - self.rect.centerx
        if abs(dist) < 300:
            self.vel.x = self.speed if dist > 0 else -self.speed
        
        self.vel.y += 0.8 
        self.move_and_collide(platforms)