import pygame, random

class Airliner(pygame.sprite.Sprite): # civil airliner class
    
    def __init__(self, game):
        super().__init__()
        self.game = game # import the Game class
        self.armor = 100 # health point
        self.max_armor = 100 # maximum health point
        self.attack = 0.3 # # point of damage in case of collision
        self.image = pygame.image.load(f'assets/airliner.png') # image recovery
        self.rect = self.image.get_rect() # retrieve the dimensions of the image
        self.rect.x = int(self.game.window_surface.get_width() + 400) # delayed appearance on a fixed point to limit the superposition with the other aircraft
        self.rect.y = random.randint(0, int(self.game.window_surface.get_height()-91)) # random appearance on the y axis
        self.velocity = random.randint(2, 3) # random movement speed       

    def damage(self, amount):
        self.armor -= amount # calculation of damage

        if self.armor <= 0: # if the airliner is destroyed
            self.game.game_over() # game over 
            self.game.defeat_type = "You destroyed an airliner." # explanation of defeat

    def update_armor_bar(self, surface): # update of the armor bar above the airliner
        pygame.draw.rect(surface, (60,60,60), [self.rect.x, self.rect.y, self.max_armor, 3]) # draw the background armor bar
        pygame.draw.rect(surface, (111,210,46), [self.rect.x, self.rect.y, self.armor, 3]) # draw the armor bar

    def move(self):
        if self.rect.x <= -100: # if the plane goes completely out of the screen
            self.game.all_airliners.remove(self) # it is destroyed
            self.game.rocket_event.attempt_shot() # trying to trigger the rockets
        elif not self.game.check_collision(self, self.game.all_planes): # if there is no collision
            self.rect.x -= self.velocity # continue normal displacement on the x axis
        else:  # if not
            self.game.plane.damage(self.attack) # damage inflicted by collision