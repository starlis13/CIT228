class GameStats:
    """Track stats for the game"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score is constant
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.playerCharacters_left = self.settings.playerCharacter_limit
        self.score = 0
        self.level = 1