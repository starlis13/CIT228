import pygame.font
from pygame.sprite import Group
from playercharacter import PlayerCharacter

class Scoreboard:
    """A class to handle scoring"""

    def __init__(self, rlm_game):
        """Initialize scoreboard fields"""
        self.rlm_game = rlm_game
        self.screen = rlm_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = rlm_game.settings
        self.stats = rlm_game.stats
        self.enemies_killed = 0

        # Font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_playerCharacters()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)   
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Display the score at the top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Center high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check for new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores, level, and playerCharacters and level on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.playerCharacters.draw(self.screen)

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        # Postion level image below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10   

    def prep_playerCharacters(self):
        """Display number of playerCharacters remaining"""
        self.playerCharacters = Group()
        for playerCharacter_number in range(self.stats.playerCharacters_left):
            playerCharacter = PlayerCharacter(self.rlm_game)
            playerCharacter.rect.x = 10 + playerCharacter_number * playerCharacter.rect.width
            playerCharacter.rect.y = 10
            self.playerCharacters.add(playerCharacter)