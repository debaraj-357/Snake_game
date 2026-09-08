import os
import time
import msvcrt

from game.food import Food
from game.board import Board
from game.snake import Snake

def main():
    board= Board()
    snake= Snake()

    food=Food(board)
    food.spawn(snake)

    score=0
    high_score=0
    starting_speed =2
    speed=starting_speed

    speed_delay={
        2:0.5,
        3:0.45,
        4:0.4,
        5:0.35,
        6:0.3,
        7:0.25,
        8:0.2
    }

    game_state = "PLAYING"
    game_running=True

    while game_running:
        print("\033[H", end="")

        if msvcrt.kbhit():
            key=msvcrt.getch().decode().lower()

            if key=="p" or key==" ":
                if game_state=="PLAYING":
                    game_state="PAUSED"
                else:
                    game_state="PLAYING"
            elif game_state=="PLAYING":
                if key=="w":
                    snake.change_direction("UP")
                elif key=="s":
                    snake.change_direction("DOWN")
                elif key =="a":
                    snake.change_direction("LEFT")
                elif key =="d":
                    snake.change_direction("RIGHT")
            

        speed= min(starting_speed+(score//50),8)

        if game_state=="PLAYING":
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
            print("\033[2J\033[H", end="")
            print()
            print("======== GAME OVER ========")
            print("snake hit itself")
            game_running=False
            continue

        if snake.body[0]==food.position or (
            food.is_big
            and snake.body[0]==(food.position[0]+1, food.position[1])
        ):    
            snake.grow()

            if food.is_big:
                score+=10
            else:
                score+=5

            if score > high_score:
                high_score=score

            food.spawn(snake)

        if game_state =="PAUSED":
            print(f"score: {score}  High Score: {high_score}   speed:{speed}")
            board.draw(snake, food)

            print()
            print("========PAUSED========")
            print("Press P or SPACE to Resume")
        else:
            print(f"score: {score}  High Score: {high_score}   speed:{speed}")
            board.draw(snake, food)    

            print(" "*30)
            print(" "*30) 
            print(" "*30)  

        time.sleep(speed_delay[speed])


if __name__=="__main__":
    main()