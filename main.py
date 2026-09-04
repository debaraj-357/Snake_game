# from game.board import Board

# def main():
#     board = Board()
#     board.draw()

# if __name__=="__main__":
#     main()

from game.snake import Snake

def main():
    snake= Snake()

    print("Before movement:")
    print(snake.body)

    snake.move()

    print("After movement:")
    print(snake.body)

if __name__=="__main__":
    main()