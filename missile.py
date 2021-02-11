import pygame

# Plane's Missile class
class Missile(pygame.sprite.Sprite):
    
    def __init__(self, plane):
        super().__init__()
        self.velocity = 9 # movement speed
        self.plane = plane # import Plane's player class
        self.attack = 50 # point of damage
        self.image = pygame.image.load('assets/missile.png') # import image
        self.rect = self.image.get_rect() # recovery of dimensions
        self.rect.x = plane.rect.x + 28 # display in the middle under the plane
        self.rect.y = plane.rect.y + 28 # display in the middle under the plane

    def move(self): # missile's mouvements
        self.rect.x += self.velocity # displacement calculation on x-axis
        if self.rect.x > self.plane.game.window_surface.get_width(): # if the missile comes out of the window
            self.plane.all_missiles.remove(self) # missile destruction
            
        for aircraft in self.plane.game.check_collision(self, self.plane.game.all_aircrafts): # for each collision with an aircraft
            self.plane.all_missiles.remove(self) # remove the missile
            aircraft.damage(self.attack) # inflict damage on the target

        for airliner in self.plane.game.check_collision(self, self.plane.game.all_airliners): # for each collision with an airliner
            self.plane.all_missiles.remove(self) # remove the missile
            airliner.damage(self.attack) # inflict damage on the target

