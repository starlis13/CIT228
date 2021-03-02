import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class template for an enemy"""

    def __init__(self, rlm_game):
        """Initialize enemy and set its starting point"""
        super().__init__()
        self.baseImage = pygame.image.load('images/enemy.png')
        self.screen = rlm_game.screen
        self.settings = rlm_game.settings

        self.image = self.baseImage
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, playerCharacter):
        """ Move enemy toward player """
        
        if self.x < playerCharacter.rect.x:
            self.image = self.baseImage
            self.x += self.settings.enemy_speed * 1
            
        if self.y < playerCharacter.rect.y:
            self.y += self.settings.enemy_speed * 1
            
        if self.x > playerCharacter.rect.x:
            self.image = pygame.transform.flip(self.baseImage, True, False)
            self.x -= self.settings.enemy_speed * 1
            
        if self.y > playerCharacter.rect.y:
            self.y -= self.settings.enemy_speed * 1
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Return True if enemy is at screen boundary"""
        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True