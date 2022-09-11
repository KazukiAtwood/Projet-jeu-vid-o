import pygame
from classe import *

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Projet jeu")
H, W = 1080, 720
screen = pygame.display.set_mode((H, W))  # 1er valeur largeur, 2eme longueur

CLOCK = pygame.time.Clock()
FPS = 100

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load('assets/mountains.png').convert()
bgPosX = background.get_width()


# charger le jeu
class Game(object):
    def __init__(self):
        self.pressed = None

    pass


game = Game()

running = True

# boucle tant que cette condition est vraie
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur souhaite aller à gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 420:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    if game.player.rect.x > 420:
        background.scroll(dx=-2)
    if background.scroll == bgPosX:
        screen.blit(background, (bgPosX, -200))
        bgPosX = + background.get_width()

    # mettre à jour l'ecran
    pygame.display.update()
    CLOCK.tick(FPS)

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # si l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
