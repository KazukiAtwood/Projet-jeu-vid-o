import pygame


# classe représentant le jeu
class Game:
    def __init__(self):
        # generer notre joueur
        self.player = Player()
        self.slime = Slime()
        self.pressed = {}

# classe représentant notre joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.player = pseudo
        self.health = 3
        self.velocity = 6
        self.image = pygame.image.load('assets/movements/standing.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 500



    def move_right(self):
        # Si le joueur n'est pas en collision avec un monstre
        if self.rect.x < 420:
            self.rect.x += self.velocity


    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity

    def get_health(self):
        return self.health



class Slime(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 1
        self.velocity = 0
        self.image = pygame.image.load('assets/slime/vert.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 501

    def get_pseudo(self):
        return self.monster

    def get_health(self):
        return self.health
