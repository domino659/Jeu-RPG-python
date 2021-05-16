from tilemap import *
from combat import *
import pygame, random
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
        self.rect.center = (x,y)
        # Velocity X and Y
        self.vel = vec(0, 0)
        # Position
        self.pos = vec(x, y)
        #Animation
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = ANIMATIONSPEED
        self.count = 0
        self.relance = 0
        self.sound = False


    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        #Movement
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.vel.x = -PLAYER_SPEED
            self.walking_anim(left_png_list)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
            self.walking_anim(right_png_list)
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.vel.y = -PLAYER_SPEED
            self.walking_anim(back_png_list)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
            self.walking_anim(front_png_list)
        # Condition to prevent diagonal movement being faster than normaly
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


        if abs(self.vel.x) > 0 or abs(self.vel.y) > 0:
            if self.sound == False:
                self.relance = pygame.time.get_ticks() + 400
                pygame.mixer.Sound(self.game.pnj_walk_sound[self.count]).play()
                self.count += 1
                self.count = self.count%10
                self.sound = True
            if pygame.time.get_ticks() > self.relance:
                self.sound = False               


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
            

    def walking_anim(self, filename):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.image = pygame.image.load(filename[self.frame])
            self.frame = (self.frame + 1) % len(left_png_list)


# Création d'un pnj
class Pnj(pygame.sprite.Sprite):
    def __init__(self, game, x, y, camera):
        self.groups = game.all_sprites, game.pnj
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Selection Sexe
        self.sex = random.randint(0,1)
        # Attribution image en fonction du sexe
        if self.sex == 0:
            self.img = PNJ_IMG_GIRL[random.randint(0, 4)]
        if self.sex == 1:
            self.img = PNJ_IMG_MALE[random.randint(0, 4)]
        self.image = pygame.image.load(self.img)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.pos = vec(x, y)
        self.speaking = False
        self.target = game.player
        self.draw_text = game.draw_text
        self.count = 1
        self.camera = camera
        self.text = random.choice(TEXTS)    

    # Interagit avec PNJ
    def interaction(self):
        if abs(self.target.rect.centerx - self.rect.centerx) < 100 and abs(self.target.rect.centery - self.rect.centery) < 100:
            self.draw_text(self.text, FONT, 10, WHITE, self.rect.centerx + self.camera.x, self.rect.y + self.camera.y, align="s")

            # Limite le son a 1 par pnj
            while (self.count <= 1):
                self.count += 1
                if self.sex == 0:
                    pygame.mixer.Sound(EFFECTS_SOUNDS['voicef']).play()
                if self.sex == 1:
                    pygame.mixer.Sound(EFFECTS_SOUNDS['voicem']).play()

            # Interaction
            if abs(self.target.rect.centerx - self.rect.centerx) < 60 and abs(self.target.rect.centery - self.rect.centery) < 60:
                # If Win dialogue           
                
                keystate = pygame.key.get_pressed()
                if keystate[INTERACT]:
                    
                    J1 = Joueur()
                    J1.classe = 'humain'
                    J1.nom = "zeubiumaru"

                    J2 = IA()
                    J2.nom="conarman"
                    i = randint(1,3)
                    print(i)
                    if i == 1 :
                        J2.sprite = ennemi1
                    elif i == 2 :
                        J2.sprite = ennemi2
                    else :
                        J2.sprite = ennemi3

                    redraw(J1,J2, 1)     
                    combat(J1,J2)
                    
                #If Win
                    self.kill()
                # If lose
                # Lose Hp, or Game over
            

class Obstacle(pygame.sprite.Sprite):
        def __init__(self, game, x, y, w, h):
            self.groups = game.walls
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.rect = pygame.Rect(x, y, w, h)
            self.x = x
            self.y = y
