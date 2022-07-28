import pygame

class Snake:
    def __init__(self, width, height):
        self.length = 2
        self.border = [width, height]
        self.body = [
                        {
                            'type': "TAIL", 
                            'position': [16,32]
                        }, 
                        {
                            'type': "HEAD", 
                            'position': [32,32]
                        }
                    ]


    def draw(self, screen):
        for part in self.body:
            if part['type'] == "HEAD":
                pygame.draw.rect(screen, "Red", pygame.Rect(part['position'][0], part['position'][1],16,16), 2) # x, y, width, heithg
            elif part['type'] == "BODY":
                pygame.draw.rect(screen, "Green", pygame.Rect(part['position'][0], part['position'][1],16,16), 2)
            elif part['type'] == "TAIL":
                pygame.draw.rect(screen, "Yellow", pygame.Rect(part['position'][0], part['position'][1],16,16), 2)
            

    def clear(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, "Black", pygame.Rect(part['position'][0], part['position'][1],16,16), 2)


    def move(self, direction):
        if direction == [0,0]:
            direction = self.generate_default_movement(direction) 

        if self.check_border(direction):
            for part in self.body:
                index = self.body.index(part)
                try: 
                    part['position'][0] = self.body[index + 1]['position'][0]
                    part['position'][1] = self.body[index + 1]['position'][1]
                except IndexError:          
                        part['position'][0] += direction[0]
                        part['position'][1] += direction[1]
            return True
        return False


    def check_border(self, direction):
        if self.body[-1]['position'][0] + direction[0] > self.border[0] or self.body[-1]['position'][0] + direction[0] < 0:
            return False
        elif self.body[-1]['position'][1] + direction[1] > self.border[1] or self.body[-1]['position'][1] + direction[1] < 0:
            return False
        return True

    
    def generate_default_movement(self, direction):
        if self.body[-1]['position'][1] == self.body[-2]['position'][1]:
            if self.body[-1]['position'][0] < self.body[-2]['position'][0]:
                direction[0] = -16
            else:
               direction[0] = 16
        else:
            if self.body[-1]['position'][1] < self.body[-2]['position'][1]:
                direction[1] = -16
            else:
                direction[1] = 16
        return direction
