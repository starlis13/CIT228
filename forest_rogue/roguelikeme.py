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

# A quick note that the working title for this game was "RogueLike_Me"
# You may see some left-over refactorings that I missed in renaming the main class here
class ForestRogue:    
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("RogueLike Me")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.playerCharacter = PlayerCharacter(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
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
        if event.key == pygame.K_RIGHT:
            self.playerCharacter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.playerCharacter.moving_left = True
        elif event.key == pygame.K_UP:
            self.playerCharacter.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.playerCharacter.moving_down = True
            
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            self._fire_in_direction('up')
        elif event.key == pygame.K_a:
            self._fire_in_direction('left')
        elif event.key == pygame.K_s:
            self._fire_in_direction('down')
        elif event.key == pygame.K_d:
            self._fire_in_direction('right')

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.playerCharacter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.playerCharacter.moving_left = False
        elif event.key == pygame.K_UP:
            self.playerCharacter.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.playerCharacter.moving_down = False
    
    def _fire_in_direction(self, direction):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, direction)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # Clear ammo when it leaves the screen (maintain memory)
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
        """Respond to bullet-enemy collisions"""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.enemies, True, True)

        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
                self.sb.enemies_killed += 1
                
            self.sb.prep_score()
            self.sb.check_high_score()
            self._create_enemies()

        # Reset game condition
        if self.sb.enemies_killed >= self.settings.level_threshold:
            self.sb.enemies_killed = 0
            self.enemies.empty()
            self.bullets.empty()
            
            self._create_enemies()
            
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_enemies(self):
        """ Check if enemy is at boundary, update enemy positions """
        self.enemies.update(self.playerCharacter)

        if pygame.sprite.spritecollideany(self.playerCharacter, self.enemies):
            self._playerCharacter_hit()

    def _playerCharacter_hit(self):
        """ Handle playerCharacter collision """
        if self.stats.playerCharacters_left > 0:
            self.stats.playerCharacters_left -= 1
            self.sb.prep_playerCharacters()

            self.enemies.empty()
            self.bullets.empty()

            self._create_enemies()
            self.playerCharacter.center_playerCharacter()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_enemies(self):
        """Create an enemy and place it in the row"""
        if len(self.enemies) <= (2 * self.stats.level):
            for enemyCount in range((2 * self.stats.level)):
                spawnPositionY = random.randint((-1 * self.settings.screen_height), self.settings.screen_height)
                spawnPositionX = random.randint((-1 * self.settings.screen_width), self.settings.screen_width)
                
                enemy = Enemy(self)
                enemy_width, enemy_height = enemy.rect.size
                enemy.x = spawnPositionX
                enemy.rect.x = enemy.x
                enemy.rect.y = spawnPositionY
                
                self.enemies.add(enemy)

    def _show_instructions(self):
        instructionsBaseImage = pygame.image.load('images/instructions.png')
        instructionRect = instructionsBaseImage.get_rect()
        instructionRect.centerx = self.screen.get_rect().centerx
        instructionRect.centery = self.screen.get_rect().centery
        self.screen.blit(instructionsBaseImage, instructionRect)

    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        self.screen.fill(self.settings.bg_color)
        self.playerCharacter.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.enemies.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
            self._show_instructions()            
            
        pygame.display.flip()
    
if __name__ == '__main__':
    rlm = ForestRogue()
    rlm.run_game()