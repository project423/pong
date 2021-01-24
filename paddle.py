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
        y = self.ycor()
        y += PADDLE_MOVE_DISTANCE
        self.sety(y)

    def paddle_down(self):
        y = self.ycor()
        y -= PADDLE_MOVE_DISTANCE
        self.sety(y)


# # Function
# def paddle_a_up():
#     y = paddle_a.ycor()
#     y += 20
#     paddle_a.sety(y)


# def paddle_a_down():
#     y = paddle_a.ycor()
#     y += -20
#     paddle_a.sety(y)

# def paddle_b_up():
#     y = paddle_b.ycor()
#     y += 20
#     paddle_b.sety(y)


# def paddle_b_down():
#     y = paddle_b.ycor()
#     y += -20
#     paddle_b.sety(y)