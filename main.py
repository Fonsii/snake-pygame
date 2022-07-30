from game_controller import GameController

WIDTH = 480
HEIGHT = 480

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()