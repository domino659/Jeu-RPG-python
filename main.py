import pygame, sys, os, math
from pygame.constants import BLEND_MAX, DROPBEGIN

from pygame.draw import aaline, rect
from pygame.event import wait
from pygame.surfarray import pixels_green 
from settings import *
from sprites import *
from tilemap import *
from pygame.locals import *


class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Init Audio
        pygame.mixer.init()
        # Init Display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Init name Window
        pygame.display.set_caption(TITLE)
        # Init game Clock
        self.clock = pygame.time.Clock()
        self.load_data()


    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    

    def load_data(self):
        self.player_img = pygame.image.load(PLAYER_IMG)


        self.effects_sounds = {}
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pygame.mixer.Sound(EFFECTS_SOUNDS[type])

        self.pnj_walk_sound = []
        for snd in PNJ_WALK_SOUND:
            s = pygame.mixer.Sound('Assets/Sounds/Walk/' + snd)
            s.set_volume(0.2)
            self.pnj_walk_sound.append(s)

        self.map = TiledMap(MAPCYBER)
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, "Assets\img")
        self.background = pygame.image.load(os.path.join(img_folder, "cp2077.jpg"))
        self.pvp = pygame.image.load(os.path.join(img_folder, "pvp.png"))
        self.play_button = pygame.image.load(os.path.join(img_folder, "playgame.png"))
        self.credits_button = pygame.image.load(os.path.join(img_folder, "credits.png"))
        self.exit_button = pygame.image.load(os.path.join(img_folder, "exit.png"))
        self.title = pygame.image.load(os.path.join(img_folder, "poitiers2077.png"))
        self.credit_bg = pygame.image.load(os.path.join(img_folder, "credit.png"))
        self.noms = pygame.image.load(os.path.join(img_folder, "nomcredits.png"))
        self.by = pygame.image.load(os.path.join(img_folder, "by.png"))
        self.font = pygame.font.SysFont("Comic sans ms, Arial", 30)
        self.text = self.font.render("(La suite)", True, BLACK)


        # avoir les rect des boutons

        # play button
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 0
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 3)

        # credits button
        self.credits_button_rect = self.credits_button.get_rect()
        self.credits_button_rect.x = 0
        self.credits_button_rect.y = math.ceil(self.screen.get_height() / 2.2)

        # exit button
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.x = math.ceil(self.screen.get_width() / 1.085)
        self.exit_button_rect.y = 10

        # title
        self.title_rect = self.title.get_rect()
        self.title_rect.x = math.ceil(self.screen.get_width() / 2.45)
        self.title_rect.y = math.ceil(self.screen.get_height() / 100)

        # text
        self.text_rect = self.text.get_rect()
        self.text_rect.x = math.ceil(self.screen.get_width() / 2.1)
        self.text_rect.y = math.ceil(self.screen.get_height() / 8)


        # by
        self.by_rect = self.by.get_rect()
        self.by_rect.x = math.ceil(self.screen.get_width() / 60)
        self.by_rect.y = math.ceil(self.screen.get_width() / 60)

        # noms
        self.noms_rect = self.noms.get_rect()
        self.noms_rect.x = math.ceil(self.screen.get_width() / 3)
        self.noms_rect.y = math.ceil(self.screen.get_width() / 8)

        # Player vs player
        self.pvp_rect = self.noms.get_rect()
        self.pvp_rect.x = 0
        self.pvp_rect.y = math.ceil(self.screen.get_width() / 3.1)


    def main_menu(self):
        inmenue = True
        while inmenue:

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.title, self.title_rect)
            self.screen.blit(self.play_button, self.play_button_rect)
            self.screen.blit(self.credits_button, self.credits_button_rect)
            self.screen.blit(self.text, self.text_rect)
            self.screen.blit(self.pvp, self.pvp_rect)
            self.draw_text("Interact: " + INTERACT_PRINT + " , Debug Collision: " + DEBUG_PRINT + ", Game Over: " + QUIT_PRINT, FONT, 20, WHITE, WIDTH / 2, HEIGHT * 7 / 8, align="center")
            self.screen.blit(self.exit_button, self.exit_button_rect)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                       inmenue = False
                    if self.credits_button_rect.collidepoint(event.pos):
                        self.credits()
                    if self.exit_button_rect.collidepoint(event.pos):
                        pygame.quit() 
                        sys.exit()
                    if self.pvp_rect.collidepoint(event.pos):
                        J1 = Joueur()
                        J1.classe = 'humain'
                        J1.nom = "Didier"

                        J2 = Joueur()
                        J2.sprite = perso2
                        J2.classe = 'humain'
                        J2.nom = "Michel"

                        redraw(J1,J2, 1)     
                        combat(J1,J2)

                
                pygame.display.flip()


    def credits(self):
        incredits = True
        while incredits:
            self.screen.blit(self.credit_bg, (0, 0))
            self.screen.blit(self.exit_button, self.exit_button_rect)
            self.screen.blit(self.by, self.by_rect)
            self.screen.blit(self.noms, self.noms_rect)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button_rect.collidepoint(event.pos):
                        self.main_menu()
                        incredits = False
            pygame.display.flip()


    # Initialize all variable and setup for new game
    def new(self):
        # Initialize Var Sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pnj = pygame.sprite.Group()
        # Set Camera
        self.camera = Camera(self.map.width, self.map.height)
        # #Load Game Sounds
        pygame.mixer.music.load(MUSICGAME)
        pygame.mixer.music.set_volume(VOLMUSICGAME)
        pygame.mixer_music.play(loops=-1)
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'pnj':
                Pnj(self, obj_center.x, obj_center.y, self.camera)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            self.draw_debug = False        


    def quit(self):
        pygame.quit()
        sys.exit()


    # Update portion of the game loop
    def update(self):
        self.all_sprites.update()
        # Camera Track Player
        self.camera.update(self.player)
        # Si je massacre tt les pnj, fin du jeu
        if len(self.pnj) == 0:
            game.show_game_win_screen()
            game.new()


    # Affichage Grid
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    def draw(self):
        # DEBUG Dessine Grid
        # self.draw_grid()

        # Map
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        # Place All_sprites in the camera zone
        for sprite in self.all_sprites:
            if isinstance(sprite, Pnj):
                sprite.interaction()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)
            pygame.draw.rect(self.screen, WHITE, self.camera.apply(self.player), 2)
        
        # Always Last action after drawing
        pygame.display.flip()


    def run(self):
        # Gamme LOOP
        self.playing = True
        while self.playing:
            # Dt -> DetlaTime (allow real time animation)
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def events(self):
        # Catch all actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == ESCAPE:
                    self.quit()
                if event.key == DEBUG:
                    self.draw_debug = not self.draw_debug
                if event.key == QUITP:
                    self.playing = False
                    self.main_menu()


    def show_start_screen(self):
        pygame.mixer.music.load(MUSICMENU)
        pygame.mixer.music.set_volume(VOLMUSICMENU)
        pygame.mixer_music.play(loops=-1)
        self.main_menu()
        
        
        # self.screen.fill(BLACK)
        # pygame.time.wait(500)
        # self.draw_text("WELCOME TO", FONT, 100, WHITE, WIDTH / 2, HEIGHT * 3 / 8, align="center")
        # self.draw_text("POITIER 2077", FONT, 100, WHITE, WIDTH / 2, HEIGHT / 2, align="center")
        # self.draw_text("Press a key to start", FONT, 75, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        # self.draw_text("Interact: " + INTERACT_PRINT + " , Debug Collision: " + DEBUG_PRINT + ", Game Over: " + QUIT_PRINT, FONT, 20, WHITE, WIDTH / 2, HEIGHT * 7 / 8, align="center")
        # pygame.display.flip()
        # self.wait_for_keys()
    

    def show_game_over_screen(self):
        pygame.mixer.music.load(MUSICMENU)
        pygame.mixer.music.set_volume(VOLMUSICMENU)
        pygame.mixer_music.play(loops=-1)
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", FONT, 100, RED, WIDTH /2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", FONT, 75, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pygame.display.flip()
        pygame.time.wait(1000)
        self.wait_for_keys()


    def show_game_win_screen(self):
        pygame.mixer.music.load(MUSICMENU)
        pygame.mixer.music.set_volume(VOLMUSICMENU)
        pygame.mixer_music.play(loops=-1)
        self.screen.fill(BLACK)
        self.draw_text("YOU WIN", FONT, 100, BLUE, WIDTH /2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", FONT, 75, WHITE, WIDTH / 2, HEIGHT * 1, align="center")
        pygame.display.flip()
        pygame.time.wait(1000)
        self.wait_for_keys()


    def wait_for_keys(self):
        pygame.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYUP:
                    waiting = False


# Create the game
game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()
    # game.show_game_over_screen()
