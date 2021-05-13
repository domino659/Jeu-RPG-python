from os import X_OK
import pygame
import pytmx
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename)
        self.tmxdata = tm
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight


    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))


    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface


class Camera:
    def __init__(self, width, height):
        # Create Rect entity of the size of the map
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0


    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)


    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)    


    def update(self, target):
        # Follow Player
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        # Limit Scrolling to Map size
        x = min(0, x) # Limite Left
        y = min(0, y) # Limite Top
        x = max(-(self.width - WIDTH), x) # Limit Right
        y = max(-(self.height - HEIGHT), y) # Limit Bottom
        self.x = x
        self.y = y
        self.camera = pygame.Rect(x, y, self.width, self.height)