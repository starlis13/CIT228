class Settings:
    
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        
        self.playerCharacter_limit = 3
        
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 2

        self.speedup_scale = 1.0
        self.score_scale = 1.5
        
        #Enemy count to level up
        self.level_threshold = 15
        self.last_level = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.playerCharacter_speed = 1.5
        self.bullet_speed = 3.0
        self.enemy_speed = 0.75
        self.enemy_points = 50

    def increase_speed(self):
        self.playerCharacter_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale