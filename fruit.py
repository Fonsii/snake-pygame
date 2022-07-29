import pygame
from random import randint


class Fruit:
    def __init__(self):
        self.position = [0, 0]


    def generate_position(self):
        self.position = [randint(0, 16) * 32, randint(0, 16) * 32]


    def draw(self, screen):
        pygame.draw.rect(screen, "Green", pygame.Rect(self.position[0], self.position[1],32,32), 2)

    
    def clear(self, screen): 
        pygame.draw.rect(screen, "Black", pygame.Rect(self.position[0], self.position[1],32,32), 2)

    