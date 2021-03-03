import pygame

class AudioManager():
    def __init__(self):
        self.ShootSound = pygame.mixer.Sound("sounds/laserBlast.flac")
        self.PlayerDeath = pygame.mixer.Sound("sounds/playerDeath.ogg")
        pygame.mixer.music.load('sounds/forest.ogg')
    
    def playBlast(self):
        pygame.mixer.Sound.play(self.ShootSound)
        
    def diePlayer(self):
        pygame.mixer.Sound.play(self.PlayerDeath)
        
    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)