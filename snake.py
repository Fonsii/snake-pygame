import pygame
from math import atan2, degrees, pi

class Snake:
    def __init__(self, width, height):
        self.length = 2
        self.border = [width, height]
        self.last_position_tail = [[32, 64]]
        self.body = [
                        {
                            'type': "TAIL", 
                            'position': [32, 64]
                        }, 
                        {
                            'type': "HEAD", 
                            'position': [64, 64],                      
                            'sprites_list':[
                                pygame.image.load('resources/snake_head/snake1.png').convert_alpha(),
                                pygame.image.load('resources/snake_head/snake2.png').convert_alpha(),
                                pygame.image.load('resources/snake_head/snake3.png').convert_alpha(),
                                pygame.image.load('resources/snake_head/snake4.png').convert_alpha(),
                                pygame.image.load('resources/snake_head/snake5.png').convert_alpha(),
                                pygame.image.load('resources/snake_head/snake6.png').convert_alpha()
                            ],
                            'current_sprite': 0,
                            'surface': 0
                        }
                    ]

        head = self.body[-1]
        head['surface'] = head['sprites_list'][head['current_sprite']]


    def draw(self, screen):
        for part in self.body:
            if part['type'] == "HEAD":
                #part['surface'] = pygame.transform.rotate(part['surface'], 90)
                screen.blit(part['surface'], part['position'])
            elif part['type'] == "BODY":
                pygame.draw.rect(screen, "White", pygame.Rect(part['position'][0], part['position'][1],32,32), 2)
            elif part['type'] == "TAIL":
                pygame.draw.rect(screen, "Yellow", pygame.Rect(part['position'][0], part['position'][1],32,32), 2)

    
    def update(self):
        head = self.body[-1]
        if head['current_sprite'] + 1 >= len(head['sprites_list']):
            head['current_sprite'] = 0
        else:
            head['current_sprite'] += 1

        head['surface'] = head['sprites_list'][head['current_sprite']]


    def move(self, direction):
        if direction == [0,0]:
            direction = self.generate_default_movement(direction) 

        if self.check_border(direction):
            for part in enumerate(self.body):
                try: 
                    if part[1]['type'] == 'TAIL' and len(self.last_position_tail) >= 2:
                        self.last_position_tail.pop()                        
                    self.last_position_tail.append(part[1]['position'])
                    
                    part[1]['position'][0] = self.body[part[0] + 1]['position'][0]
                    part[1]['position'][1] = self.body[part[0] + 1]['position'][1]
                except IndexError:   
                    part[1]['position'][0] += direction[0]
                    part[1]['position'][1] += direction[1]
                    self.update()
                    self.change_direction_head()
            return True
        return False


    def change_direction_head(self):
        head =  self.body[-1]
        element_behind_head = self.body[-2]

        change_x = element_behind_head['position'][0] - head['position'][0]
        change_y = element_behind_head['position'][1] - head['position'][1]

        radians = atan2(-change_y,change_x)
        angle = degrees(radians)

        head['surface'] =  pygame.transform.rotate(head['surface'], angle+180)


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
        self.body[0]['type'] = "BODY"
        self.body.insert(0,
            {
                'type': "TAIL", 
                'position': [0,0]
            })


    def check_border(self, direction):
        if self.body[-1]['position'][0] + direction[0] > self.border[0] or self.body[-1]['position'][0] + direction[0] < 0:
            return False
        elif self.body[-1]['position'][1] + direction[1] > self.border[1] or self.body[-1]['position'][1] + direction[1] < 0:
            return False
        return True


    def check_collision_fruit(self, fruit):
        if fruit.position[0] == self.body[-1]['position'][0] and fruit.position[1] == self.body[-1]['position'][1]:
            self.add_part_snake()
            return True
        return False
