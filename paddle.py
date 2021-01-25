from turtle import Turtle

PADDLE_MOVE_DISTANCE = 30

class Paddle(Turtle):

    def __init__(self, starting_x):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_x, 0)
    
    def paddle_up(self):
        if self.ycor() < 245:
            y = self.ycor()
            y += PADDLE_MOVE_DISTANCE
            self.sety(y)

    def paddle_down(self):
        if self.ycor() > -245:
            y = self.ycor()
            y -= PADDLE_MOVE_DISTANCE
            self.sety(y)


