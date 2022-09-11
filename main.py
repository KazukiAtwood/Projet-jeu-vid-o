import DS as DS

from classe import *

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Projet jeu")
H, W = 1080, 720
screen = pygame.display.set_mode((H, W))  # 1er valeur largeur, 2eme longueur

# définition de la zone de notre stage (partie de l'arriere plan que seul le joueur peux voir)
HW, HH = W / 2, H / 2
AREA = H * W

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load('assets/mountains.png').convert()

#  attribut la longueur et la largeur de l'arriere plan à deux variables
bgWidth, bgHeight = background.get_rect().size

# Délimition du stage.
stageWidth = bgWidth * 2

# Variable qui donne la position du joueur sur x pour que le stage puisse le suivre.
stagePosX = 0

# Déplacement de la fenêtre du stage si le joueur se déplace.
startScrollingPosX = HW

# Charger le jeu.
game = Game()

# Ne sert a rien mais a voir.
playerPosX = game.player.rect.x
playerPosY = game.player.rect.y

running = True

# Boucle tant que cette condition est vraie.
while running:

    # Appliquer l'arriere plan de notre jeu.
    screen.blit(background, (0, -200))

    # Appliquer l'image de mon joueur.
    screen.blit(game.player.image, game.player.rect)

    # Verifier si le joueur souhaite aller à gauche ou a droite.
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Reposition du joueur s'il va plus loin que le stage.
    if game.player.rect.x > stageWidth - 25:
        game.player.rect.x = stageWidth - 25
    if game.player.rect.x < 25:
        game.player.rect.x = 25
    if playerPosX < startScrollingPosX:
        circlePosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX - stageWidth + W
    else:
        circlePosX = startScrollingPosX
        stagePosX += - game.player.velocity

    rel_x = stagePosX % bgWidth
    DS.blit(game.player.image, (x, y)
    if rel_x < W:
        screen.blit(background, (rel_x, 0))

    # Pour mettre à jour l'ecran.
    pygame.display.flip()

    # Si le joueur ferme la fenetre du jeu.
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
