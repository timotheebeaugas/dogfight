import pygame

# Sound Class
class SoundManager:
    def __init__(self):
        # dict with all sound's files
        self.sounds = {
            'play': pygame.mixer.Sound('assets/sounds/main_music.ogg.'),
            'shoot': pygame.mixer.Sound('assets/sounds/air_to_air_missile.ogg.'),
            'explosion': pygame.mixer.Sound('assets/sounds/explosion.ogg.'),
            'rocket': pygame.mixer.Sound('assets/sounds/surface-to-air-missile.ogg.'),
        }

    def play(self, name, repeat=0): # play sound with name in parameter
        self.sounds[name].play(repeat)

    def stop(self, name): # play sound with name in parameter
        self.sounds[name].stop()