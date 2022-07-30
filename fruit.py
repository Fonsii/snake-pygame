import pygame
from random import randint


class Fruit:
    def __init__(self):
        self.surface = pygame.image.load('resources/fruit/apple_fruit.png').convert_alpha()
        self.rect = self.surface.get_rect()
        self.position = self.rect.move([0,0])

    def generate_position(self):
        self.position = [randint(1, 14) * 32, randint(1, 14) * 32]


    def draw(self, screen):
        screen.blit(self.surface, self.position)

    
    def clear(self, screen, world_game, surface_tiles_style): 
        x_position = int(self.position[0]/32)
        y_position = int(self.position[1]/32)
        screen.blit(surface_tiles_style[world_game[16*x_position + y_position]], [self.position[0],self.position[1]])