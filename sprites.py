import pygame
from settings import *
vec = pygame.math.Vector2

# Création d'un joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        # Velocity X and Y
        self.vel = vec(0, 0)
        # Position
        self.pos = vec(x, y)
        #Animation
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 150


    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        #Movement

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.vel.x = -PLAYER_SPEED
            self.walking(left_png_list)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
            self.walking(right_png_list)
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.vel.y = -PLAYER_SPEED
            self.walking(back_png_list)
            
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
            self.walking(front_png_list)
        # Condition to prevent diagonal movement being faster than normaly
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


    # Colide check for x and y
    def collide_with(self, dir):
        # If I hit going on the x-axis
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                # From where do I hit the wall and tell the Player he cannot go further
                # than the well (top of the wall if player is going down by example)
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        # If I hit going on the y-axis
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y


    def update(self):
        # Movement
        self.get_keys()
        self.pos += self.vel * self.game.dt
        # Check Collide
        self.rect.x = self.pos.x
        self.collide_with('x')
        self.rect.y = self.pos.y
        self.collide_with('y')


    def walking(self, filename):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.image = pygame.image.load(filename[self.frame])
            self.frame = (self.frame + 1) % len(left_png_list)


# Création d'un pnj
class Pnj(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.pnj, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.pnj_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Obstacle(pygame.sprite.Sprite):
        def __init__(self, game, x, y, w, h):
            self.groups = game.walls
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.rect = pygame.Rect(x, y, w, h)
            self.x = x
            self.y = y
            