import pygame


# Création de la classe qui va gérer la notion de monstre sur notre jeu.
class Monster(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.attack = 1
        self.image = pygame.image.load('asset/Slime bleu.png')
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 540