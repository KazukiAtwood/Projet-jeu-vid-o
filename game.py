from classe import Player
from monster import Monster
import pygame

# Créer une seconde classe qui va représenter notre jeu.
class Game :


    def __init__(self):
        # Générer notre joueur.
        self.player = Player(self)
        # Groupe de monstres.
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)



fonction
variable i qui est = à une couleur