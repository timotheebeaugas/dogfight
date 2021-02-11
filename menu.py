import pygame

# Menu class
class Menu:
    def __init__(self, game):
        self.game = game # import Game class
        self.image = pygame.image.load('assets/banner.png') # import main image
        self.rect = self.image.get_rect() # get image dimension
        self.rect.x = self.game.window_surface.get_width()/2-300 # repositioning in the middle of the screen
        self.rect.y = self.game.window_surface.get_height()/2-125 # repositioning in the middle of the screen
        self.menu_font = pygame.font.Font("assets/fonts/gunplay.ttf", 20) # Font Menu 

    def update(self): # image menu display
        self.game.window_surface.blit(self.image, self.rect)

    def instruction(self): # display of start menu text
        text = [
            "Red alert ! Our homeland is under siege by an enemy power. ",
            "You must destroy all enemy aircraft before they enter in our domestic airspace.",
            "Use ARROW KEYS to move your fighter and the SPACE BAR to fire missiles.",
            "Warning ! Don't destroy airliners and avoid the anti-aircraft missiles!",
            "Press the RETURN KEY to start the mission.",
        ]
        y_position = self.game.window_surface.get_height()/1.5 # initialize text position on y-axis
        for line in text: 
            play_text = self.menu_font.render(line, 1, self.game.default_text_color) # text rendering
            self.game.window_surface.blit(play_text, (int(self.game.window_surface.get_width()/2-(play_text.get_width()/2)), int(y_position))) # display text
            y_position += 30

    def replay(self): # display of restart menu text
        text = [
            f"Mission failure. {self.game.defeat_type}",
            "Press the RETURN KEY to try again or ESCAPE KEY to close the window.",
        ]    
        y_position = self.game.window_surface.get_height()/1.5
        for line in text: 
            play_text = self.menu_font.render(line, 1, self.game.default_text_color) # text rendering
            self.game.window_surface.blit(play_text, (int(self.game.window_surface.get_width()/2-(play_text.get_width()/2)), int(y_position))) # display text
            y_position += 30
