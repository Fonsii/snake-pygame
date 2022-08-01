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
        self.screen.fill((87,138,52))

        self.losing = False
        self.can_move_snake = True
        self.surface_tile_light = pygame.image.load('resources/tiles/layer_world_1.png').convert()
        self.surface_tile_dark = pygame.image.load('resources/tiles/layer_world_2.png').convert()
        self.font_score = pygame.font.SysFont("Garamond", 32)
        self.font_text = pygame.font.SysFont("Garamond", 30, bold=True)

        self.snake = Snake(self.width, self.height)
        self.fruit = Fruit()

        self.game()

    
    def restart_game(self):
        self.screen.fill((87,138,52))

        self.losing = False

        self.snake = Snake(self.width, self.height)
        self.fruit = Fruit()

        self.game()


    def game(self):
        self.generate_tiles_map()
        self.clock.tick(60)
        self.generate_fruit()
        self.snake.draw(self.screen)
        self.start_text_top_score()

        while True:
            if self.losing:
                self.handler_event()
            else:
                movement = self.handler_event()
                self.fruit.draw(self.screen)

                if not self.snake.move(movement):
                    self.losing = True
                    self.start_text_bottom_restart_game()
                else:
                    if self.snake.check_collision_fruit(self.fruit):
                        self.eat_fruit()
                    pygame.draw.rect(self.screen, (87,138,52), pygame.Rect(0, 0, 32, 32))
                self.snake.draw(self.screen)
                
                pygame.display.flip()
                self.generate_tiles_map()
                time.sleep(0.5)
                self.can_move_snake = True

    
    def generate_tiles_map(self):
        for x_axis in range(0,15):
            for y_axis in range(0,15):
                if (x_axis + y_axis) % 2 == 0:
                    self.screen.blit(self.surface_tile_light, [x_axis*32+32, y_axis*32+32])
                else:
                    self.screen.blit(self.surface_tile_dark, [x_axis*32+32, y_axis*32+32])


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
                    elif event.key == 114 and self.losing: # R key
                        self.restart_game()
                    elif self.can_move_snake:
                        if event.key == 119: # W key
                            movement[1] = -32
                            self.can_move_snake = False
                        elif event.key == 115: # S key
                            movement[1] = 32
                            self.can_move_snake = False
                        elif event.key == 97: # A key
                            movement[0] = -32
                            self.can_move_snake = False
                        elif event.key == 100: # D key
                            movement[0] = 32
                            self.can_move_snake = False
        return movement


    def generate_fruit(self):
        self.fruit.generate_position()
        self.fruit.draw(self.screen)
        

    def eat_fruit(self):
        self.generate_tiles_map()
        self.generate_fruit()
        self.snake.set_animation_food()
        self.snake.add_score()
        self.refresh_score()


    def start_text_top_score(self):
        fruit_icon_surface = self.fruit.surface
        self.screen.blit(fruit_icon_surface, (64,0))
        score = self.font_score.render(str(self.snake.score), False, "White")
        self.screen.blit(score, (96,0))


    def refresh_score(self):
        pygame.draw.rect(self.screen, (87,138,52), pygame.Rect(96, 0, 32, 32))
        score = self.font_score.render(str(self.snake.score), False, "White")
        self.screen.blit(score, (96,0))

    
    def start_text_bottom_restart_game(self):
        text = self.font_text.render("Press R to restart game", False, "White")
        self.screen.blit(text, (100, 510))