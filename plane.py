import pygame, random
from missile import *

# Player's Plane Class
class Plane(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game # import Game class
        self.armor = 100 # plane's armor 
        self.max_armor = 100 # # Plane's maximum armor 
        self.velocity = 5 # movement speed
        self.all_missiles = pygame.sprite.Group() # storage plane's missiles
        self.image = pygame.image.load('assets/jet.png') # import plane's image
        self.rect = self.image.get_rect() # get plane's dimensions
        self.rect.x = 10 # x-axis position
        self.rect.y = random.randint(0, int(self.game.window_surface.get_height()-91)) # random appearance on y-axis

    def damage(self, amount): # calculate damage
        if self.armor - amount > amount: # if plane's armor is not null
            self.armor -= amount # calculate damage
        else: # if the plane is destroyed
            self.game.game_over() # game over
            self.game.defeat_type = "Your fighter has been destroyed." # defeat explanation

    def update_armor_bar(self, surface): # update of the armor bar above the aircraft
        pygame.draw.rect(surface, (60,60,60), [self.rect.x, self.rect.y, self.max_armor, 3]) # draw the background armor bar
        pygame.draw.rect(surface, (111,210,46), [self.rect.x, self.rect.y, self.armor, 3]) # draw the armor bar
    
    def launch_missile(self): # new missile shot
        if self.game.is_playing: # ifgme started
            self.all_missiles.add(Missile(self)) # add  a new missile
            self.game.sound_manager.play('shoot') # play missile sound

    def move_top(self): # plane's movement
        if not self.game.check_collision(self, self.game.all_aircrafts):
            self.rect.y -= self.velocity

    def move_bottom(self):  # plane's movement
        if not self.game.check_collision(self, self.game.all_aircrafts):
            self.rect.y += self.velocity

    def move_right(self):  # plane's movement
        if not self.game.check_collision(self, self.game.all_aircrafts):
            self.rect.x += self.velocity

    def move_left(self):  # plane's movement
        if not self.game.check_collision(self, self.game.all_aircrafts):
            self.rect.x -= self.velocity