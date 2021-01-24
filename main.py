from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
wn = Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = Paddle(-350)



# Paddle B
paddle_b = Paddle(350)


# Ball
ball = Ball()


#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a.paddle_up, "w")
wn.onkeypress(paddle_a.paddle_down, "s")

wn.onkeypress(paddle_b.paddle_up, "Up")
wn.onkeypress(paddle_b.paddle_down, "Down")

#Main game loop

while True:
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
    
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)
        ball.bounce_x()

    # Paddle and ball collisions
    if ball.xcor() > 340 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):  
        ball.bounce_x()