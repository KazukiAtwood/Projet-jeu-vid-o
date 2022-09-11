import pygame



# classe représentant le jeu
class Game:
    def __init__(self):
        # generer notre joueur
        self.player = Player(self)
        # Groupe de monstre.
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)


# classe représentant notre joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.player = pseudo
        self.health = 3
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 475

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def get_health(self):
        return self.health


class Monster:
    def __init__(self, name, health):
        self.monster = name
        self.health = health

    def get_pseudo(self):
        return self.monster

    def get_health(self):
        return self.health
