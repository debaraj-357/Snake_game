class Snake:
    def __init__(self, start_x=15, start_y=15):
        self.body = [
            (start_x,start_y),
            (start_x-1,start_y),
            (start_x-2,start_y)
        ]
        self.direction="RIGHT"


    def change_direction(self,new_direction):
        if self.direction=="RIGHT" and new_direction=="LEFT":
            return
        if self.direction=="LEFT" and new_direction=="RIGHT":
            return
        if self.direction=="Up" and new_direction=="DOWN":
            return
        if self.direction=="DOWN" and new_direction=="UP":
            return

        self.direction=new_direction
        
    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head=(head_x,head_y -1)
        elif self.direction=="DOWN":
            new_head=(head_x,head_y+1)
        elif self.direction=="LEFT":
            new_head= (head_x-1, head_y)
        else:
            new_head=(head_x+1,head_y)
        self.body.insert(0,new_head)
        self.body.pop()