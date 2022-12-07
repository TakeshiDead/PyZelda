import pygame

class Weapon(pygame.sprite.Sprite):
    def _init_(self,player,groups):
    super()._init_(groups)
    self.image = pygame.Surface((40,40))