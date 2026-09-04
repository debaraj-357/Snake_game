from game.board import Board
from game.snake import Snake

def main():
    board= Board()
    snake= Snake()

    board.draw(snake)
if __name__=="__main__":
    main()