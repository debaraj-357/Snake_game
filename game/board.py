class Board:
    def __init__(self, width=30, height=30):
        self.width= width
        self.height= height

        # Light/ Medium Yellow-Brown
        self.wall_color = "\033[38;2;196;150;100m"

        #snake colors
        self.head_color="\033[31m"
        self.body_color = "\033[32m"


        self.reset_color =  "\033[0m"\

    def is_wall(self,x,y):
        return (
            x==0
            or x==self.width-1
            or y==0
            or y== self.height-1
        )
    def is_inside_playable_area(self,x,y):
        return (
            1<=x<self.width-1
            and 1<=y<self.height-1
        )
        
    def draw(self, snake=None):
        for y in range(self.height):
            line = ""

            for x in range(self.width):
                if self.is_wall(x,y):
                    line +=self.wall_color + "██" + self.reset_color

                elif snake and (x, y) == snake.body[0]:
                    line += self.head_color + "🔴" + self.reset_color

                elif snake and (x, y) in snake.body:
                    line += self.body_color + "🟢" + self.reset_color

                else:
                    line += "  "
            print(line)
