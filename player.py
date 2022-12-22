from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color('white')
        self.shapesize(stretch_wid=1.5)
        self.setheading(90)
        self.new_x = 0
        self.refresh()

    def refresh(self):
        self.goto(self.new_x, -230)

    def right_move(self):
        if self.new_x < 230:
            self.new_x += 10
        self.refresh()

    def left_move(self):
        if self.new_x > -230:
            self.new_x -= 10
        self.refresh()


