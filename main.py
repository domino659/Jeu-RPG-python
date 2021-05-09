import pygame, sys
from settings import *
from sprites import *
from tilemap import *


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


    def load_data(self):
        ###################################################
        # self.map = Map(CURRENT_MAP)
        self.map = TiledMap(MAP)
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        ###################################################

    def new(self):
        # Initialize Var Sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        # #Load Game Sounds
        pygame.mixer.music.load(MUSIC)
        pygame.mixer.music.set_volume(0.4)
        # pygame.mixer.music.set_volume(0.4)
        ###################################################
        # Construct Map
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == 'W':
        #             Wall(self, col, row)
        #         if tile == 'S':
        #             self.player = Player(self, col, row)
        # title Object -> Dictionnaire crée par txm par les Objects
        for title_object in self.map.tmxdata.objects:
            if title_object.name == 'player':
                self.player = Player(self, title_object.x, title_object.y)
            if title_object.name == 'wall':
                Obstacle(self, title_object.x, title_object.y, title_object.width, title_object.height)
            self.draw_debug = False
        # Set Camera
        self.camera = Camera(self.map.width, self.map.height)

        ###################################################



    def quit(self):
        pygame.quit()
        sys.exit()


    def events(self):
        # Catch all actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug


    def update(self):
        self.all_sprites.update()
        # Camera Track Plater
        self.camera.update(self.player)


    # Affichage Grid
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    def draw(self):
        ###################################################
        # Set couleur fond écran
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        ###################################################
        # DEBUG Dessine Grid
        # self.draw_grid()
        # Place All_sprites in the camera zone
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
             for wall in self.walls:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)
        # Always Last action after drawing
        pygame.display.flip()


    def run(self):
        # Gamme LOOP
        self.playing = True
        pygame .mixer_music.play(loops=-1)
        while self.playing:
            # Dt -> DetlaTime (allow real time animation)
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()



    def show_start_screen(self):
        pass


    def show_game_over_screen(self):
        pass


# Create the game
game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()
    game.show_go_screen()