from game_controller import GameController

WIDTH = 500
HEIGHT = 500

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()