import time
import msvcrt

from game.food import Food
from game.board import Board
from game.snake import Snake
from game.menu import Menu

# ===========================
# RESTART 
# ===========================

def game_over_screen(score, high_score):

    print()
    print("========GAME OVER ========")
    print()
    print(f"Final Score: {score}")
    print(f"High Score: {high_score}")
    print()
    print("R. Restart Game")
    print("M. Main Menu")

    while True:
        choice = input("enter your choice: ").lower()

        if choice =="r":
            return "RESTART"
        elif choice =="m":
            return "MENU"
        else:
            print("Invalid choice. Please enter R or M.")
        
def play_game(starting_speed, high_score):
        # ===========================
        # GAME SETUP
        # ===========================
    
        print("\033[2J\033[H", end="")
    
        board = Board()
        snake = Snake()
    
        food = Food(board)
        food.spawn(snake)
    
        score=0
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
        
    
        # ===========================
        # GAME LOOP
        # ===========================
    
        while True:
            print("\033[H", end = "")
    
            # ===========================
            # KEYBOARD INPUT
            # ===========================
    
            if msvcrt.kbhit():
                key=msvcrt.getch().decode().lower()
    
                if key == "p" or key == " ":
                    if game_state == "PLAYING":
                        game_state = "PAUSED"
                    else:
                        game_state = "PLAYING"
    
                elif game_state == "PLAYING":
                    if key == "w":
                        snake.change_direction("UP")
                    elif key == "s":
                        snake.change_direction("DOWN")
                    elif key == "a":
                        snake.change_direction("LEFT")
                    elif key == "d":
                        snake.change_direction("RIGHT")
                
    
            # ===========================
            # SPEED SYSTEM
            # ===========================
    
            speed= min(starting_speed+(score//50),8)
    
            # ===========================
            # MOVEMENT
            # ===========================
    
            if game_state == "PLAYING":
                 snake.move()
           
            # ===========================
            # WALL COLLISION
            # ===========================
    
            head_x, head_y = snake.body[0]
    
            if board.is_wall(head_x,head_y):

                if score > high_score:
                    high_score=score

                print("\033[2J\033[H", end="")
                print("Snake hit the wall")
    
                result = game_over_screen(score, high_score)

                return result, high_score
    
            # ===========================
            # SELF COLLISION
            # ===========================
    
            head = snake.body[0]
    
            if head in snake.body[1:]:

                if score>high_score:
                    high_score=score

                print("\033[2J\033[H", end="")
                print("snake hit itself")
    
                result= game_over_screen(score, high_score)
                return result, high_score
    
            #===========================
            # FOOD
            #===========================
    
            if snake.body[0] == food.position or (
                food.is_big
                and snake.body[0] == (food.position[0]+1, food.position[1])
            ):    
                snake.grow()
    
                if food.is_big:
                    score += 10
                else:
                    score += 5
    
                if score > high_score:
                    high_score = score
    
                food.spawn(snake)
    
            # ===========================
            # DISPLAY
            # ===========================
    
            if game_state == "PAUSED":
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
    



def main():

    menu = Menu()

    starting_speed = 2
    high_score = 0


    # ===========================
    # MAIN MENU
    # ===========================

    # Application Loop
    while True:

        # Main Menu 
        while True:
                choice = menu.show()
                
                if choice == "1":
                    print("Starting Game.....")
                    time.sleep(0.5)
                    break
                
                elif choice == "2":
                    starting_speed=menu.select_speed()
                    print(f"Speed {starting_speed} selected")
                    time.sleep(0.5)
                
                elif choice == "3":
                    print()
                    print("========HIGH SCORE ========")
                    print()
                    print(f"High Score: {high_score}")
                    print()
                    input("Press Enter to return to Main Menu")
                
                    
                elif choice == "4":

                    print("\033[2J\033[H", end="")

                    print("===========================")
                    print("        HOW TO PLAY        ")
                    print("===========================")

                    print("CONTROLS")
                    print()
                    print("W    -> Move UP")
                    print("S    -> Move Down")
                    print("A    -> Move Left")
                    print("D    -> Move Right")
                    print()

                    print("FOOD")
                    print()
                    print("Normal Food -> +5 points")
                    print("Big Food -> +10 points")
                    print()

                    print("SPEED")
                    print()
                    print("Speed automatically increases")
                    print("by 1 every 50 points.")
                    print("Maximum speed is 8.")
                    print()

                    print("COLLISION")
                    print()
                    print("Hit Wall -> Game Over")
                    print("Hit Body -> Game Over")
                    print()

                    print("RULE")
                    print()
                    print("You cannot immediately reverse")
                    print("the snake's direction")
                    print()

                    print("-------------------------------------")
                    input("Press enter to return to Main Menu")
                                        
                elif choice == "5":
                    print("Exiting Game...")
                    return
        
            # ===========================
            # GAME SESSION
            # ===========================
        
        while True:
            result, high_score = play_game(
            starting_speed,
            high_score
            )
        
            if result == "RESTART":
                continue
            elif result == "MENU":
                break



if __name__ == "__main__":
    main()