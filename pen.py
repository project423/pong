from turtle import Turtle


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.score_a = 0
        self.score_b = 0
        self.write(f"{self.score_a}  {self.score_b}", align="center", font=("Courier", 36, "normal"))
    
    def add_one_a(self):
        self.score_a += 1
        self.update_score()

    def add_one_b(self):
        self.score_b += 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"{self.score_a}  {self.score_b}", align="center", font=("Courier", 36, "normal"))

    def game_over(self):
        if self.score_a > self.score_b:
            self.clear()
            self.goto(0, 30)
            self.write(f" Game Over", align="center", font=("Courier", 24, "normal"))
            self.goto(0, 0)
            self.write(f"{self.score_a}  {self.score_b}", align="center", font=("Courier", 24, "normal"))
            self.goto(0, -30)
            self.write(f"Player 1 Wins", align="center", font=("Courier", 24, "normal"))
        else:
            self.clear()
            self.goto(0, 0)
            self.write(f" Game Over\n {self.score_a}  {self.score_b}\nPlayer 2 Wins", align="center", font=("Courier", 24, "normal"))
        


    
    
    