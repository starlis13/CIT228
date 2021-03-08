import sys
import pygame
import random

from time import sleep
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from playercharacter import PlayerCharacter
from bullet import Bullet
from enemy import Enemy
from audiomanager import AudioManager

# Credits:
# A lot of the base code is mocked from the Crash Course Python book
# Laser Sprites: https://opengameart.org/content/lasers-and-beams
# Player Character (Rogue): https://opengameart.org/content/animated-rogue
# Background (slightly edited): https://opengameart.org/content/small-leaves-texture
# Laser sound: https://opengameart.org/content/insect-or-alien-scream-short
# Background Music: https://opengameart.org/content/creepy-forest-f
# Character death: https://opengameart.org/content/8bit-death-whirl

# A quick note that the working title for this game was "RogueLike_Me"
# You may see some left-over refactorings that I missed in renaming the main class here
class ForestRogue:    
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        self.background = pygame.image.load("images/bg.jpg")
        
        pygame.display.set_caption("Forest Rogue")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.playerCharacter = PlayerCharacter(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        self.audioManager = AudioManager()
        self.audioManager.playBackgroundMusic()
        self.play_button = Button (self, "Play")


    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.playerCharacter.update()
                self._update_bullets()
                self._update_enemies()
                
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_playerCharacters()

            self.enemies.empty()
            self.bullets.empty()
            self._create_enemies()
            
            self.playerCharacter.center_playerCharacter()
            pygame.mouse.set_visible(False)
            
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.playerCharacter.moving_right = True
        elif event.key == pygame.K_a:
            self.playerCharacter.moving_left = True
        elif event.key == pygame.K_w:
            self.playerCharacter.moving_up = True
        elif event.key == pygame.K_s:
            self.playerCharacter.moving_down = True
            
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self._fire_in_direction('up')
        elif event.key == pygame.K_LEFT:
            self._fire_in_direction('left')
        elif event.key == pygame.K_DOWN:
            self._fire_in_direction('down')
        elif event.key == pygame.K_RIGHT:
            self._fire_in_direction('right')


    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.playerCharacter.moving_right = False
        elif event.key == pygame.K_a:
            self.playerCharacter.moving_left = False
        elif event.key == pygame.K_w:
            self.playerCharacter.moving_up = False
        elif event.key == pygame.K_s:
            self.playerCharacter.moving_down = False
    
    
    def _fire_in_direction(self, direction):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, direction)
            self.bullets.add(new_bullet)
            self.audioManager.playBlast()


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.direction == 'up' and bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            if bullet.direction == 'down' and bullet.rect.bottom >= self.settings.screen_height:
                self.bullets.remove(bullet)
            if bullet.direction == 'left' and bullet.rect.x <= 0:
                self.bullets.remove(bullet)
            if bullet.direction == 'right' and bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_enemy_collisions()
                        

    def _check_bullet_enemy_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
                self.sb.enemies_killed += 1
                
            self.sb.prep_score()
            self.sb.check_high_score()
            self._create_enemies()

        if self.sb.enemies_killed >= self.settings.level_threshold:
            self.sb.enemies_killed = 0
            self.settings.increase_speed()
            
            if self.stats.level < self.settings.last_level:
                self.stats.level += 1
                self.sb.prep_level()
            else:
                self.stats.game_active = False


    def _update_enemies(self):
        self.enemies.update(self.playerCharacter)

        if pygame.sprite.spritecollideany(self.playerCharacter, self.enemies):
            self._playerCharacter_hit()


    def _playerCharacter_hit(self):
        if self.stats.playerCharacters_left > 0:
            self.stats.playerCharacters_left -= 1
            self.sb.prep_playerCharacters()

            self.enemies.empty()
            self.bullets.empty()
            self._create_enemies()
            
            self.playerCharacter.center_playerCharacter()
            self.audioManager.diePlayer()

            sleep(2.2)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _create_enemies(self):
        if len(self.enemies) <= (2 * self.stats.level):
            for enemyCount in range((2 * self.stats.level)):
                spawnPositionY = random.randint(0, (self.settings.screen_height / 2))
                spawnPositionX = random.randint(0, (self.settings.screen_width / 2))
                
                enemy = Enemy(self)
                enemy_width, enemy_height = enemy.rect.size
                
                enemy.x = spawnPositionX
                enemy.rect.x = enemy.x
                enemy.y = spawnPositionY
                enemy.rect.y = enemy.y
                
                self.enemies.add(enemy)


    def _show_image(self, imageName):
        instructionsBaseImage = pygame.image.load(imageName)
        instructionRect = instructionsBaseImage.get_rect()
        instructionRect.centerx = self.screen.get_rect().centerx
        instructionRect.centery = self.screen.get_rect().centery
        self.screen.blit(instructionsBaseImage, instructionRect)


    def _update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.playerCharacter.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.enemies.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active and self.stats.level < self.settings.last_level:
            self.play_button.draw_button()
            self._show_image('images/instructions.png')
        elif not self.stats.game_active and self.stats.level == self.settings.last_level and len(self.sb.playerCharacters) >= 0:
            self._show_image('images/youwon.png')
            
        pygame.display.flip()
    
if __name__ == '__main__':
    rlm = ForestRogue()
    rlm.run_game()