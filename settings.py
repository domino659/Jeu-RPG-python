import pygame

# Basic Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)


# Game settings
WIDTH = 1920 
HEIGHT = 1080 
# Get Screen Info
# screen = pygame.display.set_mode()
# WIDTH, HEIGHT = screen.get_size()


FPS = 60
TITLE = "Jeux d'Insultes"
MAP = 'Map/map.tmx'
MAP_back = 'Map/map_back.tmx'
FONT = 'Assets/Font/SuperLegendBoy.ttf'

# Music Track
MUSIC = 'Assets/Music/Not Giving Up.ogg'
MUSICMENU = 'Assets/Music/Adventure Begin.ogg'

# Sounds
EFFECTS_SOUNDS = {'voice': 'Assets/Sounds/attack1.wav'}

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


# Player Setting
PLAYER_SPEED = 300
PLAYER_IMG = 'Assets/Actor/hero/front2.png'

# PNJ
PNJ_IMG = 'Assets/Actor/pnj/pnj1.png'
PNJ_BRONTIS = 'Assets/Actor/pnj/feebrontis.png'


front_png_list = ['Assets/Actor/hero/front1.png', 'Assets/Actor/hero/front2.png', 'Assets/Actor/hero/front3.png']
back_png_list = ['Assets/Actor/hero/back1.png', 'Assets/Actor/hero/back2.png', 'Assets/Actor/hero/back3.png']
right_png_list = ['Assets/Actor/hero/right1.png', 'Assets/Actor/hero/right2.png','Assets/Actor/hero/right3.png']
left_png_list = ['Assets/Actor/hero/left1.png', 'Assets/Actor/hero/left2.png','Assets/Actor/hero/left3.png']