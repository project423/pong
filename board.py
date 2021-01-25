from turtle import Turtle

LINE_SPACING = 20

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(3)
        self.color("white")
        self.penup()
        self.goto(0, -310)
        self.setheading(90)
        self.draw_line()
        

    def draw_line(self):
        for _ in range(800 // (LINE_SPACING * 2)):
            self.pendown()
            self.forward(LINE_SPACING)
            self.penup()
            self.forward(LINE_SPACING)
            