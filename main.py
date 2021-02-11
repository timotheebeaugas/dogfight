# -*- coding: utf-8 -*-
import pygame, datetime
from game import *

pygame.init() # initialize pygame

window_surface = pygame.display.set_mode((0, 0)) # Creates the plot window in full screen

game = Game(window_surface) # load the Game class and pass the window as a parameter

loop = True # true value to trigger the main loop endlessly 

while loop: # Main even t wihle

    window_surface.fill((30, 30, 30)) # gray background

    if game.is_playing: # if the game is started
        game.update() # update the game
    else: # if the game has not started
        game.main_menu() # display the main menu

    for event in pygame.event.get(): # browse the list of events
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: # leave the game
            running = False # stop the loop
            pygame.quit() # close pygame
        elif event.type == pygame.KEYDOWN: # check the keys pressed
            game.pressed[event.key] = True # if it is pressed go the value on True
            if event.key == pygame.K_RETURN: 
                game.start() # start the game
                game.sound_manager.play('play') # start main background music
            if event.key == pygame.K_SPACE:
                game.plane.launch_missile() # launch the missile
        elif event.type == pygame.KEYUP: # if the key is up
            game.pressed[event.key] = False # go the value on False
    
    pygame.display.flip() # update the display




