from game_controller import GameController

WIDTH = 512
HEIGHT = 512

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()