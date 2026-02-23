import pygame
from settings import *
from entities.player import Player
from entities.enemy import Enemy
from world.tilemap import World
from engine.camera import Camera

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sila Challenge - Jour 6")
    clock = pygame.time.Clock()

    # Initialisation du monde et des entités
    world = World("world/level1.json")
    player = Player(100, 100)
    # On passe les dimensions du monde à la caméra pour les limites (clamping)
    camera = Camera(world.width, world.height)
    enemy = Enemy(500, 100)

    running = True
    while running:
        # 1. Gestion des entrées
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # 2. Mise à jour (Update)
        # On passe 'keys' pour les contrôles et 'world.platforms' pour les collisions
        player.update(keys, world.platforms)
        enemy.update(player, world.platforms)
        
        # La caméra suit le joueur
        camera.follow(player)

        # 3. Affichage (Draw)
        screen.fill(BLUE) # Assure-toi que BLUE est défini dans settings.py

        # Dessiner le monde en premier (fond)
        world.draw(screen, camera)

        # Dessiner les entités avec l'offset de la caméra
        screen.blit(player.image, camera.apply(player.rect))
        screen.blit(enemy.image, camera.apply(enemy.rect))

        pygame.display.flip()
        
        # Limite à 60 FPS pour une physique constante
        clock.tick(FPS) 

    pygame.quit()

if __name__ == "__main__":
    main()