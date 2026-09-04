class Board:
    def __init__(self, width=30, height=30):
        self.width= width
        self.height= height

        # Light/ Medium Yellow-Brown
        self.wall_color = "\033[38;2;196;150;100m"
        self.reset_color =  "\033[0m"\
        
    def draw(self):
        for row in range(self.height):
            line = ""

            for column in range(self.width):
                if (
                    row ==0
                    or row == self.height-1
                    or column == 0
                    or column == self.width-1
                ):
                    line += self.wall_color + "██" + self.reset_color
                else:
                    line += "  "
            print(line)
