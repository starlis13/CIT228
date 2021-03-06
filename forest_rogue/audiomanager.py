import pygame
import os

class AudioManager():
    def __init__(self):
        self.ShootSound = pygame.mixer.Sound("sounds/laserBlast.flac")
        pygame.mixer.Sound.set_volume(self.ShootSound, 0.2)
        
        self.PlayerDeath = pygame.mixer.Sound("sounds/playerDeath.ogg")
        pygame.mixer.Sound.set_volume(self.PlayerDeath, 0.4)
        
        self.base_track = pygame.mixer.Sound("sounds/forest.ogg")
        pygame.mixer.Sound.set_volume(self.base_track, 0.1)
        pygame.mixer.Sound.play(self.base_track)
    
    def playBlast(self):
        pygame.mixer.Sound.play(self.ShootSound)
        
    def diePlayer(self):
        pygame.mixer.Sound.play(self.PlayerDeath)
        
    def playBackgroundMusic(self):
        pygame.mixer.Sound.play(self.base_track, loops=-1)