import pygame
from rocket import Rocket

# Rocket even Class
class RocketShootEvent:
    # lors du chargement, crer un compteur
    def __init__(self, game):
        self.game = game # import Game class
        self.percent = 0 # 0% loading
        self.percent_speed = 15 # loading speed
        self.shot_mode = False # is shot mode actived
        self.all_rockets = pygame.sprite.Group() # rocket group

    def add_percent(self): # loading bar 
        self.percent += self.percent_speed/100

    def is_full_loaded(self): # check load bar
        return self.percent >= 100
    
    def reset_percent(self): # reset load bar
        self.percent = 0

    def rocket_shot(self): # trigger rocket fire
        self.game.sound_manager.play('rocket') # play rocket sound
        for i in range(20): # add new rockets
            self.all_rockets.add(Rocket(self))

    def attempt_shot(self): # try to launch rocket
        # if the event gauge is fully charged and the aircraft have disappeared
        if self.is_full_loaded() and len(self.game.all_aircrafts) == 0 and len(self.game.all_airliners) == 0:
            self.shot_mode = True # activer l'évènement
            self.rocket_shot() # launch rockets

    def update_bar(self, surface): #update load bar
        self.add_percent() # increment load bar

        # black baground (black color)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # x-axis
            0, # y-axis
            surface.get_width(), # width 100%
            5 # thickness
        ])
        # load bar (red color)
        pygame.draw.rect(surface, (255, 0, 0), [
            0, # x-axis
            0, # y-axis
            (surface.get_width()/100)*self.percent, # width 100%
            5 # thickness
        ])

