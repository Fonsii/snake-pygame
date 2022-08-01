import pygame
from math import atan2, degrees, pi

class Snake:
    def __init__(self, width, height):
        self.length = 2
        self.border = [width, height]
        self.score = 0
        self.default_animation_head_snake = [
            pygame.image.load('resources/snake_head/snake1.png').convert_alpha(),
            pygame.image.load('resources/snake_head/snake2.png').convert_alpha(),
            pygame.image.load('resources/snake_head/snake3.png').convert_alpha(),
            pygame.image.load('resources/snake_head/snake4.png').convert_alpha(),
            pygame.image.load('resources/snake_head/snake5.png').convert_alpha(),
            pygame.image.load('resources/snake_head/snake6.png').convert_alpha()
        ]
        self.eating_animation_head_snake = [
            pygame.image.load('resources/snake_head_fruit/snake_food1.png').convert_alpha(),
            pygame.image.load('resources/snake_head_fruit/snake_food2.png').convert_alpha(),
            pygame.image.load('resources/snake_head_fruit/snake_food3.png').convert_alpha(),
            pygame.image.load('resources/snake_head_fruit/snake_food4.png').convert_alpha()
        ]

        self.body = [
                        {
                            'type': "TAIL", 
                            'position': [32, 64],
                            'surface':  pygame.image.load('resources/snake_tail/snake_tail.png').convert_alpha(),
                            'default_surface': pygame.image.load('resources/snake_tail/snake_tail.png').convert_alpha()
                        }, 
                        {
                            'type': "HEAD", 
                            'position': [64, 64],                      
                            'sprites_list': self.default_animation_head_snake,
                            'current_sprite': 0,
                            'surface': 0,
                            'eating' : False
                        }
                    ]

        head = self.body[-1]
        head['surface'] = head['sprites_list'][head['current_sprite']]


    def draw(self, screen):
        for part in self.body:
            screen.blit(part['surface'], part['position'])

    
    def update(self):
        head = self.body[-1]
        if head['current_sprite'] + 1 >= len(head['sprites_list']):
            if head['eating']:
                self.set_animation_default()
            head['current_sprite'] = 0
        else:
            head['current_sprite'] += 1

        head['surface'] = head['sprites_list'][head['current_sprite']]


    def move(self, direction):
        if direction == [0,0] or self.check_movement_behind(direction):
            direction = self.generate_default_movement(direction) 

        if self.check_collision_border(direction) and self.check_collision_body_parts(direction):
            for part in enumerate(self.body):
                try: 
                    part[1]['position'][0] = self.body[part[0] + 1]['position'][0]
                    part[1]['position'][1] = self.body[part[0] + 1]['position'][1]
                except IndexError:   
                    part[1]['position'][0] += direction[0]
                    part[1]['position'][1] += direction[1]
                    self.update()
                    self.change_directions()
            return True
        return False


    def change_directions(self):
        for part in enumerate(self.body):
            if part[1]['type'] == "HEAD":
                self.change_direction_head()
            elif part[1]['type'] == "TAIl":
                self.change_direction_tail()
            else:
                self.change_direction_body(part[0], part[1])


    def change_direction_head(self):
        head =  self.body[-1]
        element_behind_head = self.body[-2]

        change_x = element_behind_head['position'][0] - head['position'][0]
        change_y = element_behind_head['position'][1] - head['position'][1]

        radians = atan2(-change_y,change_x)
        angle = degrees(radians)

        head['surface'] =  pygame.transform.rotate(head['surface'], angle+180)


    def change_direction_tail(self):
        tail =  self.body[0]
        element_ahead_tail = self.body[1]

        change_x = tail['position'][0] - element_ahead_tail['position'][0]
        change_y = tail['position'][1] - element_ahead_tail['position'][1]

        radians = atan2(-change_y,change_x)
        angle = degrees(radians)

        tail['surface'] = pygame.transform.rotate(tail['default_surface'], angle+180)


    def change_direction_body(self, body_index, body_part):
        element_ahead_tail = self.body[body_index + 1]

        change_x = body_part['position'][0] - element_ahead_tail['position'][0]
        change_y = body_part['position'][1] - element_ahead_tail['position'][1]

        radians = atan2(-change_y,change_x)
        angle = degrees(radians)

        body_part['surface'] = pygame.transform.rotate(body_part['default_surface'], angle+180)


    def generate_default_movement(self, direction):
        if self.body[-1]['position'][1] == self.body[-2]['position'][1]:
            if self.body[-1]['position'][0] < self.body[-2]['position'][0]:
                direction[0] = -32
            else:
               direction[0] = 32
        else:
            if self.body[-1]['position'][1] < self.body[-2]['position'][1]:
                direction[1] = -32
            else:
                direction[1] = 32
        return direction


    def add_part_snake(self):
        new_part = {
            'type': "BODY",
            'position': self.body[0]['position'],
            'surface': pygame.image.load('resources/snake_body/snake_body.png').convert_alpha(),
            'default_surface': pygame.image.load('resources/snake_body/snake_body.png').convert_alpha(),
        }

        self.body.insert(1, new_part)
        self.body[0]['position'] = [0,0]

    
    def set_animation_food(self):
        head = self.body[-1]
        head['sprites_list'] = self.eating_animation_head_snake
        head['current_sprite'] = 0
        head['eating'] = True


    def set_animation_default(self):
        head = self.body[-1]
        head['sprites_list'] = self.default_animation_head_snake
        head['eating'] = False


    def check_collision_border(self, direction):
        head = self.body[-1]
        if head['position'][0] + direction[0] > self.border[0] - 32 or head['position'][0] + direction[0] < 0:
            return False
        elif head['position'][1] + direction[1] > self.border[1] - 32  or head['position'][1] + direction[1] < 0:
            return False
        return True

    def check_collision_body_parts(self, direction):
        head = self.body[-1]
        for part in self.body[:-1]:
            if head['position'][0] + direction[0] == part['position'][0] and head['position'][1] + direction[1] == part['position'][1]:
                return False
        return True


    def check_movement_behind(self, direction):
        head = self.body[-1]
        element_behind_head = self.body[-2]
        if head['position'][0] + direction[0] == element_behind_head['position'][0] and head['position'][1] + direction[1] == element_behind_head['position'][1]:
            return True
        return False


    def check_collision_fruit(self, fruit):
        if fruit.position[0] == self.body[-1]['position'][0] and fruit.position[1] == self.body[-1]['position'][1]:
            self.add_part_snake()
            return True
        return False

    
    def add_score(self):
        self.score += 1