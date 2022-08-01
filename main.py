from game_controller import GameController

WIDTH = 544
HEIGHT = 544

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()