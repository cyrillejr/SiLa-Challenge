import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0) 
        self.rect = pygame.Rect(x, y, w, h)
        self.on_ground = False

    def move_and_collide(self, tiles):
        self.pos.x += self.vel.x
        self.rect.x = int(self.pos.x)
        hits = [t for t in tiles if self.rect.colliderect(t)]
        for tile in hits:
            if self.vel.x > 0:
                self.rect.right = tile.left
            elif self.vel.x < 0:
                self.rect.left = tile.right
            self.pos.x = self.rect.x
            self.vel.x = 0

        self.on_ground = False
        self.pos.y += self.vel.y
        self.rect.y = int(self.pos.y)
        hits = [t for t in tiles if self.rect.colliderect(t)]
        for tile in hits:
            if self.vel.y > 0:
                self.rect.bottom = tile.top
                self.on_ground = True
                self.vel.y = 0
            elif self.vel.y < 0:
                self.rect.top = tile.bottom
                self.vel.y = 0
            self.pos.y = self.rect.y