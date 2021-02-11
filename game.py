import pygame, datetime
from plane import *
from aircraft import *
from sound import *
from airliner import *
from menu import *
from rocket_event import RocketShootEvent

# Game class
class Game:

    def __init__(self, window_surface):
        self.window_surface = window_surface # recovery of the playing surface
        self.is_playing = False # game status
        self.is_first_play = True # status of the first part playing
        # generate the player's plane
        self.all_planes = pygame.sprite.Group()
        self.plane = Plane(self)
        self.all_planes.add(self.plane)
        # generate enemy aircraft
        self.all_aircrafts = pygame.sprite.Group()
        # generate airliners
        self.all_airliners = pygame.sprite.Group()
        # storage of keys pressed by the player's keyboard
        self.pressed = {}
        # import the events class
        self.rocket_event = RocketShootEvent(self)
        # default text parameter
        self.caption_font = pygame.font.Font("assets/fonts/gunplay.ttf", 15) # Font
        self.default_text_color  = (255, 250, 250) # text color
        self.score = 0 # score initialization
        # import sound class
        self.sound_manager = SoundManager()
        self.level = 1 # current playing level
        self.clock = pygame.time.Clock() # get time clock
        self.menu = Menu(self) # pass parameters from game to menu class
        self.defeat_type = "" # description of the type of defeat

    def main_menu(self): # menu display
        self.menu.update() # main image
        if self.is_first_play: # if this is the first part
            self.menu.instruction() # show all instructions
        else: # if not
            self.menu.replay() # propose to replay

    def start(self): # start of the game
        self.is_playing = True 
        self.is_first_play = False
        self.creat_aircrafts() # creation of aircraft

    def game_over(self): # game over
        # put the game back as at the beginning
        self.sound_manager.stop('play') # stop main music
        self.sound_manager.stop('rocket') # stop rockets sound
        self.all_aircrafts = pygame.sprite.Group() # empty the group
        self.all_airliners= pygame.sprite.Group() # empty the group
        self.rocket_event.all_rockets = pygame.sprite.Group() # empty the group
        self.plane.armor = self.plane.max_armor
        self.rocket_event.reset_percent() 
        self.is_playing = False
        self.score = 0
        self.level = 1

    def check_collision(self, sprite, group): # checks for collision between aircraft
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def level_up(self): # increase by one level of difficulty
        self.level += 1

    def creat_aircrafts(self): # aircraft creation
        for i in range(self.level): # create drones for all levels
            self.all_aircrafts.add(Reaper(self))
        for i in range(int(self.level/2)): 
            if self.level >= 2:
                self.all_airliners.add(Airliner(self)) # create airliner from level 2
            if self.level >= 3:
                self.all_aircrafts.add(F117(self)) # create bomber from level 3
        if self.level >= 4:
            self.all_aircrafts.add(B2(self)) # create bomber from level 4

    def update(self): # update display

        self.clock.tick(60) # 60 frames per second of the game

        score_text = self.caption_font.render(f"Score : {self.score}", 1, self.default_text_color  ) # score recovery
        level_text = self.caption_font.render(f"Level : {self.level}", 1, self.default_text_color  ) # level recovery
        game_time = str(datetime.timedelta(milliseconds=pygame.time.get_ticks())).split(".")[0] # conversion of time to total time 
        display_fps = self.caption_font.render(f"{self.clock.get_fps():.2f} FPS", 1, self.default_text_color  ) # calculate FPS
        display_time = self.caption_font.render(f"{game_time}", 1, self.default_text_color  ) # total game time recovery

        self.window_surface.blit(score_text, (20, 20)) # score display
        self.window_surface.blit(level_text, (120, 20)) # level display
        self.window_surface.blit(display_time, [220, 20]) # time display
        self.window_surface.blit(display_fps, [int(self.window_surface.get_width()-90), 20]) # FPS display

        self.all_aircrafts.draw(self.window_surface) # draw the aircraft
        self.all_airliners.draw(self.window_surface) # draw the airliners
        self.plane.all_missiles.draw(self.window_surface) # draw plane's missiles
        self.plane.update_armor_bar(self.window_surface) # draw plane armor
        self.window_surface.blit(self.plane.image, self.plane.rect) # drow plane
        self.rocket_event.all_rockets.draw(self.window_surface) # draw all the rockets

        for missile in self.plane.all_missiles: # for each missiles
            missile.move() # shifting

        for aircraft in self.all_aircrafts: # for each aircrafts
            aircraft.move() # shifting
            aircraft.update_armor_bar(self.window_surface) # update armor bar

        for airliner in self.all_airliners: # for each ailiners
            airliner.move() # shifting
            airliner.update_armor_bar(self.window_surface) # update armor bar

        for rocket in self.rocket_event.all_rockets: # for each rockets
            rocket.shot() # shifting

        self.rocket_event.update_bar(self.window_surface) # refresh the game event bar

        # check the active keys to order the movement of the player's plane 
        if self.pressed.get(pygame.K_UP) and self.pressed.get(pygame.K_RIGHT) and self.plane.rect.y > 0 and self.plane.rect.x + self.plane.rect.width < self.window_surface.get_width():
            self.plane.move_top()
            self.plane.move_right()
        elif self.pressed.get(pygame.K_UP) and self.pressed.get(pygame.K_LEFT) and self.plane.rect.y > 0 and self.plane.rect.x > 0:
            self.plane.move_top()
            self.plane.move_left()
        elif self.pressed.get(pygame.K_DOWN) and self.pressed.get(pygame.K_LEFT) and self.plane.rect.y + self.plane.rect.width < self.window_surface.get_height() and self.plane.rect.x > 0:
            self.plane.move_bottom()
            self.plane.move_left()
        elif self.pressed.get(pygame.K_DOWN) and self.pressed.get(pygame.K_RIGHT) and self.plane.rect.y + self.plane.rect.width < self.window_surface.get_height() and self.plane.rect.x + self.plane.rect.width < self.window_surface.get_width():
            self.plane.move_bottom()
            self.plane.move_right()
        elif self.pressed.get(pygame.K_RIGHT) and self.plane.rect.x + self.plane.rect.width < self.window_surface.get_width():
            self.plane.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.plane.rect.x > 0:
            self.plane.move_left()
        elif self.pressed.get(pygame.K_UP) and self.plane.rect.y > 0:
            self.plane.move_top()
        elif self.pressed.get(pygame.K_DOWN) and self.plane.rect.y + self.plane.rect.width < self.window_surface.get_height():
            self.plane.move_bottom() 
            


