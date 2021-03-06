import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, rlm_game, direction = 'up'):
        super().__init__()
        self.screen = rlm_game.screen
        self.settings = rlm_game.settings
        self.direction = direction
        
        if self.direction == 'up':
            self.image = pygame.image.load('images/magic_bolt.png')
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(pygame.image.load('images/magic_bolt.png'), 180)
        elif self.direction == 'left':
            self.image = pygame.transform.rotate(pygame.image.load('images/magic_bolt.png'), 90)
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(pygame.image.load('images/magic_bolt.png'), -90)
            
        self.rect = self.image.get_rect()
        
        self.rect.midtop = rlm_game.playerCharacter.rect.midtop
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        if self.direction == 'up':
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
        elif self.direction == 'down':
            self.y += self.settings.bullet_speed
            self.rect.y = self.y
        elif self.direction == 'left':
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x
        elif self.direction == 'right':
            self.x += self.settings.bullet_speed
            self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)