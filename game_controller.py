from sys import exit
import pygame
import time

from snake import Snake
from fruit import Fruit

class GameController:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        
    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.width, self.height)
        self.fruit = Fruit()

        self.game()

    
    def game(self):
        self.snake.draw(self.screen)
        self.generate_fruit()
        self.clock.tick(60)

        while True:
            movement = self.handler_event()

            self.snake.clear(self.screen)
            self.snake.move(movement)

            if self.snake.check_collision_fruit(self.fruit):
                self.generate_fruit()
                self.snake.move([0,0])

            self.snake.draw(self.screen)


            pygame.display.flip()
            time.sleep(0.5)

    
    def handler_event(self):
        movement = [0,0]
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pygame.quit()
                        exit()
                    elif event.key == 119: # W key
                        movement[1] = -32
                    elif event.key == 115: # S key
                        movement[1] = 32
                    elif event.key == 97: # A key
                        movement[0] = -32
                    elif event.key == 100: # D key
                        movement[0] = 32
        return movement


    def generate_fruit(self):
        self.fruit.clear(self.screen)
        self.fruit.generate_position()
        self.fruit.draw(self.screen)


    def eat_fruit(self):
        pass