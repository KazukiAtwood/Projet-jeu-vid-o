import pygame

# Créer une classe qui va gérer la notion de monstre sur notre jeu.
class Monster :


    def __init__(self):
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.image = pygame.image.load('assets/slime/vert.png')
        self.rect = self.image.get_rect()