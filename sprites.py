import pygame
from settings import *

# Création d'un joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        # Velocity X and Y
        self.vx, self.vy = 0, 0
        # Self Position
        self.x = x #* TILESIZE
        self.y = y #* TILESIZE


    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        #Movement
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.vx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.vy = -PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = PLAYER_SPEED
        # Condition to prevent diagonal movement being faster than normaly
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071


    # Colide check for x and y
    def collide_with(self, dir):
        # If I hit going on the x-axis
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                # From where do I hit the wall and tell the Player he cannot go further
                # than the well (top of the wall if player is going down by example)
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        # If I hit going on the y-axis
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y


    def update(self):
        # Movement
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # Check Collide
        self.rect.x = self.x
        self.collide_with('x')
        self.rect.y = self.y
        self.collide_with('y')

###################################################
# Création des murs
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Obstacle(pygame.sprite.Sprite):
        def __init__(self, game, x, y, w, h):
            self.groups = game.walls
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.rect = pygame.Rect(x, y, w, h)
            self.x = x
            self.y = y
            self.rect.x = x
            self.rect.y = y

###################################################