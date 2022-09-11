import pygame

# Class représentant notre joueur.
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        # self.player = pseudo
        self.game = game
        self.health = 3
        self.max_health = 3
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self):
        # Si le joueur n'est pas en collision avec une entité
        if self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def get_health(self):
        return self.health