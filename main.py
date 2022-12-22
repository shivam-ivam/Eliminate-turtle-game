from turtle import Screen
from player import Player
from bullet import Bullet
import time
from enemy import Enemy
from scoreboard import Score


screen = Screen()
screen.title("Save the side")
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.tracer(0)
player = Player()
bullet = Bullet()
enemy = Enemy()
score = Score()


def new_bullet():
    x_cor = player.xcor()
    bullet.create_bullet(x_cor)


screen.listen()
screen.onkeypress(key='d', fun=player.right_move)
screen.onkeypress(key='a', fun=player.left_move)
screen.onkey(key='space', fun=new_bullet)

live = 3
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.01)
    bullet.fire()
    enemy.create_enemy()
    enemy.move_enemies()
    for i in enemy.enemies_list:
        if i.ycor() < -224:
            enemy.enemies_list.remove(i)
            i.hideturtle()
            score.lost()
            live -= 1
            if live <= 0 :
                game_is_on = False
        for j in bullet.bullets:
            if j.distance(i) < 15:
                enemy.kill_enemy(i)
                bullet.strike_bullet(j)
                score.scored()






screen.exitonclick()




