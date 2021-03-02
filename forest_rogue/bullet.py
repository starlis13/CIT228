import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to handle playerCharacter bullets"""

    def __init__(self, ai_game, direction = 'up'):
        """Create a bullet at the playerCharacter's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
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

        # Create a bullet rect at (0, 0), then set correct position
        #self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.rect.midtop = ai_game.playerCharacter.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet vertically"""
        # Update the decimal position of the bullet
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
        """Draw the bullet to the screen"""
        #pygame.draw.rect(self.image, self.rect)
        self.screen.blit(self.image, self.rect)