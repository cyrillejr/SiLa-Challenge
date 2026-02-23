import pygame
from entities.base import Entity
from settings import PLAYER_SPEED, JUMP_FORCE

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 48)
        self.image = pygame.Surface((32, 48))
        self.image.fill((255, 0, 0))
        self.vel_y = 0
        self.vel_x = 0
        self.on_ground = False

    def update(self, keys, platforms):
        self.handle_input(keys)
        
        # Mouvement X
        self.rect.x += self.vel_x
        self.check_collisions(platforms, 'horizontal')
        
        # Mouvement Y (Gravité)
        self.vel_y += 0.8 # Gravité
        self.rect.y += self.vel_y
        self.on_ground = False # Reset avant check
        self.check_collisions(platforms, 'vertical')

    def handle_input(self, keys):
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_FORCE

    def check_collisions(self, platforms, direction):
        for wall in platforms:
            if self.rect.colliderect(wall):
                if direction == 'horizontal':
                    if self.vel_x > 0: self.rect.right = wall.left
                    if self.vel_x < 0: self.rect.left = wall.right
                if direction == 'vertical':
                    if self.vel_y > 0:
                        self.rect.bottom = wall.top
                        self.vel_y = 0
                        self.on_ground = True
                    if self.vel_y < 0:
                        self.rect.top = wall.bottom
                        self.vel_y = 0