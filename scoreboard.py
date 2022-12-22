from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.highScore = 0
        # with open('highscore.txt', mode='r') as file:
        #     self.highScore = int(file.read())
        self.live = 3
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-210, 220)
        self.write(f'Score: {self.score}', align='center', font=('arial', 12, 'normal'))
        self.goto(180, 220)
        self.write(f'High Score: {self.highScore}', align='center', font=('arial', 12, 'normal'))
        self.goto(0, 220)
        heart = ''
        for i in range(1, self.live+1):
            heart += ' 💞 '
        self.write(f'{heart}', align='center', font=('arial', 12, 'normal'))

    def scored(self):
        self.score += 1
        if self.highScore < self.score:
            self.highScore = self.score
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.highScore))
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('arial', 20, 'bold'))
        self.goto(0, -20)
        self.write(f'Score: {self.score}', align='center', font=('arial', 12, 'normal'))

    def lost(self):
        self.live -= 1
        self.refresh()
        if self.live <= 0:
            self.game_over()


