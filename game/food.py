import random

class Food:
    def __init__(self,board):
        self.board=board
        self.position =None


    def spawn(self,snake):
        while True:
            x=random.randint(1,self.board.width - 2)
            y=random.randint(1, self.board.height - 2)

            position=(x,y)

            if position not in snake.body:
                self.position=position
                break