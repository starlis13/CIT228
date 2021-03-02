import pygame
from pygame.sprite import Sprite

class PlayerCharacter(Sprite):
    def __init__(self, roguelikeme):
        super().__init__()
        self.baseImage = pygame.image.load('images/playerCharacter.png')
        self.screen = roguelikeme.screen
        self.settings = roguelikeme.settings
        self.screen_rect = roguelikeme.screen.get_rect()

        self.image = self.baseImage
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Set the character's movement boundaries - i.e. we don't want the character leaving the screen """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = self.baseImage
            self.x += self.settings.playerCharacter_speed
        
        if self.moving_left and self.rect.left > 0:
            self.image = pygame.transform.flip(self.baseImage, True, False)
            self.x -= self.settings.playerCharacter_speed
        
        if self.moving_up and self.rect.top > 0:
             self.y -= self.settings.playerCharacter_speed
             
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
             self.y += self.settings.playerCharacter_speed

        # Allow motion along the vertical and lateral axis
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_playerCharacter(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)