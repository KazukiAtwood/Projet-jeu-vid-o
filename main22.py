from classe import *
from pygame import gfxdraw as gfx
from random import *

pygame.init()

# variable
running = True
walkCount = 0
CLOCK = pygame.time.Clock()
FPS = 100
a = -2000
i = 0

# generer la fenetre de notre jeu
pygame.display.set_caption("Enigma")
H, W = 1080, 720
screen = pygame.display.set_mode((H, W))  # 1er valeur largeur, 2eme longueur
# fixation des limites de la fenêtre de notre jeu
offset_x, offset_y = 0, 0
poly = screen.get_rect()
polypoints = (poly.topleft, poly.topright, poly.bottomright, poly.bottomleft)

# arrière plan titre
bg1 = pygame.image.load('assets/backgrounds/TITRE.jpg')

# chargement des différents arrières plan de notre jeu
background = pygame.image.load('assets/backgrounds/BG_1.jpg').convert()
bg = [pygame.image.load('assets/backgrounds/BG_2.jpg').convert(),
      pygame.image.load('assets/backgrounds/BG_3.jpg').convert(),
      pygame.image.load('assets/backgrounds/BG_4.jpg').convert()]

# importer ou charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4

# importer ou charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 3.33
play_button_rect.y = screen.get_height() / 2

# chargement sprite joueur déplacement
walkRight = [pygame.image.load('assets/movements/R1.png'), pygame.image.load('assets/movements/R2.png'),
             pygame.image.load('assets/movements/R3.png'), pygame.image.load('assets/movements/R4.png'),
             pygame.image.load('assets/movements/R5.png'), pygame.image.load('assets/movements/R6.png'),
             pygame.image.load('assets/movements/R7.png'), pygame.image.load('assets/movements/R8.png'),
             pygame.image.load('assets/movements/R9.png')]

walkLeft = [pygame.image.load('assets/movements/L1.png'), pygame.image.load('assets/movements/L2.png'),
            pygame.image.load('assets/movements/L3.png'), pygame.image.load('assets/movements/L4.png'),
            pygame.image.load('assets/movements/L5.png'), pygame.image.load('assets/movements/L6.png'),
            pygame.image.load('assets/movements/L7.png'), pygame.image.load('assets/movements/L8.png'),
            pygame.image.load('assets/movements/L9.png')]

# charger le jeu
game = Game()

# boucle tant que cette condition est vraie
while running:
    # si le joueur atteint la limite du scrolling alors redéfinissions en 0
    if offset_x < -32700:
        offset_x = 0


    # compteur de marche
    if walkCount + 1 >= 27:
        walkCount = 0

    # changement d'arriere plan si le joueur atteint une position en x
    if offset_x < a and i != 3:
        background = bg[i]
        a = a - 2000
        i = i + 1

    # appliquer l'arrière plan de notre jeu
    gfx.textured_polygon(screen, polypoints, background, offset_x, offset_y)


    # Chargement image barre de vie.
    health_bar = pygame.image.load('assets/vie2.jpg')

    # Monstre slime
    if game.player.rect.x > 100:
        screen.blit(game.slime.image, game.slime.rect)

    transition = pygame.image.load("assets/backgrounds/ecran.jpg").convert()


    # verifier si le joueur souhaite aller à gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
        offset_x -= 5
        screen.blit(walkRight[walkCount // 3], game.player.rect)
        walkCount += 1
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
        screen.blit(walkLeft[walkCount // 3], game.player.rect)  # We integer divide walkCount by 3 to ensure each
        walkCount += 1  # image is shown 3 times every animation
    # si joueur ne bouge pas, appliquer l'image par défaut
    else:
        screen.blit(game.player.image, game.player.rect)

    print(game.player.rect.x)

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