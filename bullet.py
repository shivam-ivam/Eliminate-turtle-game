import time
from turtle import Turtle


class Bullet:

    def __init__(self):
        self.bullets = []

    def create_bullet(self, x_cor):
        new_bullet = Turtle()
        new_bullet.setheading(90)
        new_bullet.penup()
        new_bullet.goto(x=x_cor, y=-220)
        new_bullet.shape("circle")
        new_bullet.color('white')
        new_bullet.shapesize(stretch_wid=.5, stretch_len=1)
        self.bullets.append(new_bullet)

    def fire(self):
        for i in self.bullets:
            i.forward(5)
            if i.ycor() > 300:
                i.hideturtle()
                self.bullets.remove(i)

    def strike_bullet(self, bullet_strike):
        bullet_strike.hideturtle()
        self.bullets.remove(bullet_strike)








