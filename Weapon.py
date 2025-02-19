import pygame

class Weapon(pygame.sprite.Sprite):
    def _init_(self,player,groups):
    super()._init_(groups)
    direction = player.status.split('_')[0]

    # graphic
    full_path = f'PATH OF THE WEAPONS HERE{player.weapon}/{direction}.png'
    self.image = pygame.image.loud(full_path).convert_alpha()

    #placement
    if direction == 'right':
        self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
    elif direction == 'left':
        self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
    elif direction == 'down':
         self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
    else:
        self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))