from classe import *

pygame.init()

# Générer la fenetre de notre jeu
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

# délimitation du stage
stageWidth = bgWidth * 2

# variable qui donne la position du joueur sur x pour que le stage puisse le suivre
stagePosX = 0

# déplace la fenêtre du stage si le joueur se déplace
startScrollingPosX = HW

# charger le jeu
game = Game()

# ne sert a rien mais a voir
playerPosX = game.player.rect.x
playerPosY = game.player.rect.y

running = True

# boucle tant que cette condition est vraie
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur souhaite aller à gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # reposition du joueur s'il va plus loin que le stage
    if playerPosX > stageWidth - 100:
        game.player.rect.x = stageWidth - 100
    if playerPosX < startScrollingPosX:
        game.player.rect.x = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX:
        game.player.rect.x = playerPosX - stageWidth + W
    else:
        game.player.rect.x = startScrollingPosX
        stagePosX += - game.player.velocity

    rel_x = stagePosX % bgWidth
    screen.blit(background, (rel_x - bgWidth, -200))
    if rel_x < W:
        screen.blit(background, (rel_x, -200))

    # mettre à jour l'ecran
    pygame.display.update()

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
