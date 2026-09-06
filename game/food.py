import random

class Food:
    def __init__(self,board):
        self.board=board
        self.position =None
        self.food_count=0
        self.is_big=False


    def spawn(self,snake):
        self.food_count+=1

        if self.food_count%11==0:
            self.is_big=True
        else:
            self.is_big=None

        while True:
            if self.is_big:
                x=random.randint(1,self.board.width-3)
            else:
                x=random.randint(1,self.board.width - 2)

            y=random.randint(1, self.board.height - 2)

            position=(x,y)

            if self.is_big:
                second_position=(x+1,y)

                if position not in snake.body and second_position not in snake.body:
                    self.position=position
                    break
            else:
                if position not in snake.body:
                    self.position=position
                    break   