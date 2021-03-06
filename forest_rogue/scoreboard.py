import pygame.font
from pygame.sprite import Group
from playercharacter import PlayerCharacter

class Scoreboard:
    def __init__(self, rlm_game):
        self.rlm_game = rlm_game
        self.screen = rlm_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = rlm_game.settings
        self.stats = rlm_game.stats
        self.enemies_killed = 0

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_playerCharacters()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)   
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.playerCharacters.draw(self.screen)

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10   

    def prep_playerCharacters(self):
        self.playerCharacters = Group()
        for playerCharacter_number in range(self.stats.playerCharacters_left):
            playerCharacter = PlayerCharacter(self.rlm_game)
            playerCharacter.rect.x = 10 + playerCharacter_number * playerCharacter.rect.width
            playerCharacter.rect.y = 10
            self.playerCharacters.add(playerCharacter)