from turtle import Turtle
import winsound
from random import randint

class Ball(Turtle):
    def __init__(self, dx):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.dx = dx
        self.dy = .25
        
    
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1
        #sound
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    def bounce_y(self):
        self.dy *= -1
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


