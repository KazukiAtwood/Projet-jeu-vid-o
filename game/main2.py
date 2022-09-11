from classe import *
from pygame.locals import *

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Projet jeu")
H, W = 1080, 720
screen = pygame.display.set_mode((H, W))  # 1er valeur largeur, 2eme longueur

CLOCK = pygame.time.Clock()
FPS = 100

# importer de charger l'arriere plan de notre jeu
bg = pygame.image.load('mountains.png').convert()

# charger le jeu
game = Game()

bgX = 0
bgX2 = bg.get_width()
spriteX = game.player.image.get_width()


def redrawscreen():
    if game.player.rect.x == 420:
        screen.blit(bg, (bgX, -200))
        screen.blit(bg, (bgX2, -200))
    screen.blit(game.player.image, game.player.rect)
    pygame.display.update()


pygame.time.set_timer(USEREVENT + 1, 500)
# appliquer l'image de mon joueur
running = True

# boucle tant que cette condition est vraie
while running:

    redrawscreen()
    CLOCK.tick(FPS)
    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    # appliquer l'arriere plan de notre jeu
    screen.blit(bg, (0, -200))

    # verifier si le joueur souhaite aller à gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 420:
        game.player.move_right()
        print(game.player.rect.x)
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # si l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier (a enlever)
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
