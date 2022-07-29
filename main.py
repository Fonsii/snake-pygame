from game_controller import GameController

WIDTH = 528
HEIGHT = 528

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()