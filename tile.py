import pygame
from settings import *

class Title(pygame.sprite.Sprite):
    def _init_(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE)))
    super()._init_(groups)
    self.sprite_type = sprite_type
    self.image = surface
    if Sprite_type =='object':
        self.rect = self.image.get_rect(topleft = (pos[0],pos[1]- TILESIZE))
    else:
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)