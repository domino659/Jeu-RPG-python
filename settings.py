import pygame

# Get Screen Info
SCREEN = pygame.display.set_mode()
WIDTH, HEIGHT = SCREEN.get_size()

# Screen settings
# WIDTH = 1920 
# HEIGHT = 1080

# WIDTH = 1280
# HEIGHT = 720

# Input
ESCAPE = pygame.K_ESCAPE
DEBUG = pygame.K_h
INTERACT = pygame.K_e
QUIT = pygame.K_p
# Input Guide
DEBUG_PRINT = 'H'
INTERACT_PRINT = 'E'
QUIT_PRINT = 'P'

FPS = 60
TITLE = "Jeux Type RPG"
MAP = 'Map/map.tmx'
MAPCYBER = 'Map/cyber.tmx'
FONT = 'Assets/Font/SuperLegendBoy.ttf'

# Music Track
MUSICGAME = 'Assets/Music/Not Giving Up.ogg'
VOLMUSICGAME = 0.2
MUSICMENU = 'Assets/Music/Adventure Begin.ogg'
VOLMUSICMENU = 0.2

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player Setting
PLAYER_SPEED = 200
ANIMATIONSPEED = 150
PLAYER_IMG = 'Assets/Actor/hero/front2.png'

# PNJ
PNJ_IMG_GIRL = ['Assets/Actor/pnj/pnjgirl0.png', 'Assets/Actor/pnj/pnjgirl1.png', 'Assets/Actor/pnj/pnjgirl2.png', 'Assets/Actor/pnj/pnjgirl3.png', 'Assets/Actor/pnj/pnjgirl4.png']
PNJ_IMG_MALE = ['Assets/Actor/pnj/pnjmale0.png', 'Assets/Actor/pnj/pnjmale1.png', 'Assets/Actor/pnj/pnjmale2.png', 'Assets/Actor/pnj/pnjmale3.png', 'Assets/Actor/pnj/pnjmale4.png']    

# Text
TEXTS = ['Hello Traveler', 'You want to fight', 'Bring it on !', "I'm a Pnj, yes I know that my life has no meaning", 'It smells like Game Over!']

# Sounds
EFFECTS_SOUNDS = {'voicef': 'Assets/Sounds/voicef.wav',
                  'voicem': 'Assets/Sounds/voicem.wav'}

PNJ_WALK_SOUND = ['walk0.wav', 'walk1.wav', 'walk2.wav', 'walk3.wav', 'walk4.wav', 'walk5.wav', 'walk6.wav', 'walk7.wav', 'walk8.wav', 'walk9.wav']

# Player Imgs
front_png_list = ['Assets/Actor/hero/front1.png', 'Assets/Actor/hero/front2.png', 'Assets/Actor/hero/front3.png']
back_png_list = ['Assets/Actor/hero/back1.png', 'Assets/Actor/hero/back2.png', 'Assets/Actor/hero/back3.png']
right_png_list = ['Assets/Actor/hero/right1.png', 'Assets/Actor/hero/right2.png','Assets/Actor/hero/right3.png']
left_png_list = ['Assets/Actor/hero/left1.png', 'Assets/Actor/hero/left2.png','Assets/Actor/hero/left3.png']

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