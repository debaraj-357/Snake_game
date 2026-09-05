import os
import time
import msvcrt

from game.board import Board
from game.snake import Snake

def main():
    board= Board()
    snake= Snake()

    game_running=True

    while game_running:
        print("\033[H", end="")

        if msvcrt.kbhit():
            key=msvcrt.getch().decode().lower()

            if key=="w":
                snake.change_direction("UP")
            elif key=="s":
                snake.change_direction("DOWN")
            elif key =="a":
                snake.change_direction("LEFT")
            elif key =="d":
                snake.change_direction("RIGHT")

        
        snake.move()
        board.draw(snake)

        time.sleep(0.5)


if __name__=="__main__":
    main()