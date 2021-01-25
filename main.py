from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from pen import Pen
from board import Board
wn = Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

WINNING_SCORE = 10

#Draw Board
board = Board()

# Paddle A
paddle_a = Paddle(-350)

# Paddle B
paddle_b = Paddle(350)

# Ball
ball1 = Ball(-.25)
# ball2 = Ball(.25)
# ball3 = Ball(-.5)
# ball4 = Ball(.5)

balls = [ball1]

#Pen
pen = Pen()


#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a.paddle_up, "w")
wn.onkeypress(paddle_a.paddle_down, "s")

wn.onkeypress(paddle_b.paddle_up, "Up")
wn.onkeypress(paddle_b.paddle_down, "Down")

#Main game loop
game_is_on = True
while game_is_on:
    for ball in balls:
        wn.update()

        #Move the ball
        ball.move()
        
        

        #Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.bounce_y()

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.bounce_y()
        
        if ball.xcor() > 390:
            pen.add_one_a()
            ball.goto(0,0)
            ball.bounce_x()
        
        if ball.xcor() < -390:
            pen.add_one_b()
            ball.goto(0,0)
            ball.bounce_x() 

        # Paddle and ball collisions
        #Collision with paddle B
        if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)  
            ball.bounce_x()

        #Collision with paddle B
        if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)  
            ball.bounce_x()

        if pen.score_a == WINNING_SCORE:
            pen.game_over()
            game_is_on = False
        
        if pen.score_b == WINNING_SCORE:
            pen.game_over()
            game_is_on = False

        #AI Player
        # closet_ball = balls[1]
        # for ball in balls:
        #     if ball.xcor() < closet_ball.xcor():
        #         closet_ball = ball

        # if paddle_a.ycor() < closet_ball.ycor() and abs(paddle_a.ycor() - closet_ball.ycor()) > 10:
        #     paddle_a.paddle_up()
        
        # elif paddle_a.ycor() > closet_ball.ycor() and abs(paddle_a.ycor() - closet_ball.ycor()) > 10:
        #     paddle_a.paddle_down()


wn.exitonclick()