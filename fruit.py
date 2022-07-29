import pygame
from random import randint


class Fruit:
    def __init__(self):
        self.surface = pygame.image.load('resources/fruit/apple_fruit.png').convert()
        self.rect = self.surface.get_rect()
        self.position = self.rect.move([0,0])

    def generate_position(self):
        self.position = [randint(1, 16) * 32, randint(1, 16) * 32]


    def draw(self, screen):
        screen.blit(self.surface, self.position)

    
    def clear(self, screen): 
        pygame.draw.rect(screen, "Black", pygame.Rect(self.position[0], self.position[1],32,32))