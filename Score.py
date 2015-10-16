__author__ = 'Polle'
import Highscore
class Score:
    CurrentScore = 25
    Time = 0
    GAMESTATE = "NOTSTARTED"
    def __init__(self):
        pass

    def aftrek(self, hoeveel, label):
        self.CurrentScore -= hoeveel
        if self.CurrentScore <= 0:
            self.CurrentScore = 0
            self.gameOver(self)
        #print("Score: " + str(self.CurrentScore))
        label.set(str(self.CurrentScore))

    def checkForGameOver(self):
        if self <= 0:
            return True
        else:
            return False

    def getScore(self):
        return self.CurrentScore

    def startGame(self):
        self.GAMESTATE = "STARTED"

    def winGame(self, score, name):
        self.GAMESTATE = "WIN"
        highscore = Highscore.Highscore(name, score.getScore(), self.Time)
        highscore.save()

    def gameOver(self, score):
        self.GAMESTATE = "GAMEOVER"