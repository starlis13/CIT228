import pygame.font

class Button:
    """ Button template to draw interactive controls """

    def __init__(self, rlm_game, msg):
        """Initialize button"""
        self.screen = rlm_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of a button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Consolas', 48)

        # Build a button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += 400

        # Prepare button object
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Create button and prepare the button content"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and its content"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)