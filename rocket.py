import pygame, random

# Rocket class
class Rocket(pygame.sprite.Sprite):

    def __init__(self, rocket_event):
        super().__init__()        
        self.rocket_event = rocket_event # import rocket even Class
        self.image = pygame.image.load('assets/rocket.png') # import rocket image
        self.rect = self.image.get_rect() # get rocket dimension
        self.velocity = random.randint(6, 14) # random movement speed
        self.attack = 33 # power attack 
        self.rect.x = random.randint(0, int(self.rocket_event.game.window_surface.get_width()-91)) # random position on the x-axis 
        self.rect.y = random.randint(int(self.rocket_event.game.window_surface.get_height()+91), int(self.rocket_event.game.window_surface.get_height()+910)) # random position on the x-axis with depth of field to spread the range of appearance

    def remove(self): # remove rocket
        self.rocket_event.all_rockets.remove(self) # remove rocket

        if len(self.rocket_event.all_rockets) == 0: # if there is no rocket
            self.rocket_event.reset_percent() # reset event bar
            self.rocket_event.game.level_up() # add a new level
            self.rocket_event.game.creat_aircrafts() # creat new aircraft
                
    def shot(self): # launch rockets
        self.rect.y -= self.velocity # calculate movement 
        if self.rect.y <= -100: # if rocket is outside window
            self.remove() # remove rocket
            if len(self.rocket_event.all_rockets) == 0: # if all rockets are removed
                self.rocket_event.reset_percent() # reset event bar
                self.rocket_event.shot_mode = False # block shot mode

        # if collision with player's plane
        if self.rocket_event.game.check_collision(
            self, self.rocket_event.game.all_planes
        ):
            self.remove() # destroy rocket 
            self.rocket_event.game.plane.damage(self.attack) # apply damages
