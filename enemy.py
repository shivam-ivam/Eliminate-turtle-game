from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan']


class Enemy:

    def __init__(self):
        self.enemies_list = []

    def create_enemy(self):

        if len(self.enemies_list) < 5: 
            new_enemy = Turtle()
            new_enemy.penup()
            new_enemy.shape('turtle')
            new_enemy.color(random.choice(COLORS))
            new_enemy.goto(random.randint(-220, 220), 250)
            new_enemy.setheading(270)
            self.enemies_list.append(new_enemy)

    def move_enemies(self):
        for i in self.enemies_list:
            i.forward(.6)

    def kill_enemy(self, kill_enemy):
        kill_enemy.hideturtle()
        self.enemies_list.remove(kill_enemy)



