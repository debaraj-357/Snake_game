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

        head_x, head_y = snake.body[0]

        if board.is_wall(head_x,head_y):
            print("\033[2J\033[H", end="")
            print()
            print("======== GAME OVER ========")
            print("Snake hit the wall")
            game_running=False
            continue

        head = snake.body[0]

        if head in snake.body[1:]:
            print("\033[2j\033[H", end="")
            print()
            print("======== GAME OVER ========")
            game_running=False
            continue
        board.draw(snake)

        time.sleep(0.5)


if __name__=="__main__":
    main()