import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.KEY_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0


        if keys[pygame.K_RIGHT]:
            self.direction.X = -1
        elif keys[pygame.KEY_LEFT]:
            self.direction.X = 1
        else:
            self.direction.X = 0

    def move(self, speed):
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)
        #https://youtu.be/QU1pPzEGrqw?t=2197
