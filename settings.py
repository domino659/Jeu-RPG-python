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
CYAN = (0,255,255)

# Game settings
# WIDTH = 1920 
# HEIGHT = 1080 
# Get Screen Info
screen = pygame.display.set_mode()
WIDTH, HEIGHT = screen.get_size()

FPS = 60
TITLE = "Jeux d'Insultes"
MAP = 'Map/map.tmx'
# Music Track
MUSIC = 'Assets/Sounds/Not Giving Up.ogg'

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player Setting
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
PLAYER_SPEED = 600




