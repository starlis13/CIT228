class GameStats:
    def __init__(self, rlm_game):
        self.settings = rlm_game.settings
        self.reset_stats()
        
        self.game_active = False
        
        self.high_score = 0

    def reset_stats(self):
        self.playerCharacters_left = self.settings.playerCharacter_limit
        self.score = 0
        self.level = 1