import pygame, random

class Aircraft(pygame.sprite.Sprite): # enemy aircraft class
    
    def __init__(self, game, name, score, defense): # pass aircraft characteristics in parameters
        super().__init__()
        self.game = game # import the Game class
        self.armor = 100 # health points
        self.max_armor = 100 # maximum point
        self.defense = defense # defense point to reduce enemy attack 
        self.attack = 0.3 # attack point for collisions
        self.image = pygame.image.load(f'assets/{name}.png') # image import
        self.rect = self.image.get_rect() # retrieve image dimensions
        self.rect.x = random.randint(self.game.window_surface.get_width(), int(self.game.window_surface.get_width()+300)) # random position on the x-axis with depth of field to avoid overlapping
        self.rect.y = random.randint(0, int(self.game.window_surface.get_height()-91)) # random position on the y axis
        self.score = score # gained points if the object is destroyed

    def set_speed(self, speed): 
        self.default_speed = speed # random speed for each respawn 
        self.velocity = random.randint(1, speed) # random speed for the start the game        

    def damage(self, amount):
        self.armor -= int(amount / self.defense) # calculation of damage inflicted on the aircraft

        # if the armor level is 0
        if self.armor <= 0:
            # # recreate a new aircraft
            self.game.sound_manager.play('explosion') # play an explosion sound
            self.rect.x = self.game.window_surface.get_width()
            self.rect.y = random.randint(0, int(self.game.window_surface.get_height()-91))
            self.velocity = random.randint(1,self.default_speed)
            self.armor = self.max_armor
            self.game.score += self.score # adding points to the score

            if self.game.rocket_event.is_full_loaded(): # if the event bar is 100% loaded
                self.game.all_aircrafts.remove(self) # deletion of aircraft
                self.game.rocket_event.attempt_shot() # try to trigger the rockets

    def update_armor_bar(self, surface): # update of the armor bar above the aircraft
        pygame.draw.rect(surface, (60,60,60), [self.rect.x, self.rect.y, self.max_armor, 3]) # draw the background armor bar
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x, self.rect.y, self.armor, 3]) # draw the armor bar

    def move(self): #p lane movement
        if self.rect.x <= 0: # if a plane manages to exit the screen
            self.game.game_over() # game over
            self.game.defeat_type = "An enemy aircraft has entered our airspace." # defeat explanation
            self.game.rocket_event.attempt_shot() # try to trigger the rockets
        elif not self.game.check_collision(self, self.game.all_planes): # if there is no collision
            self.rect.x -= self.velocity # continue normal displacement on the x axis
        else:  # if not
            self.game.plane.damage(self.attack) # damage inflicted by collision


# Reaper drone class
class Reaper(Aircraft):

    def __init__(self, game):
        super().__init__(game, 'drone', 1, 1)
        self.set_speed(4)

# light stealth bomber class
class F117(Aircraft):

    def __init__(self, game):
        super().__init__(game, 'f117', 2, 2)
        self.set_speed(2)

# strategic stealth bomber class
class B2(Aircraft):

    def __init__(self, game):
        super().__init__(game, 'b2', 3, 3)
        self.set_speed(1)