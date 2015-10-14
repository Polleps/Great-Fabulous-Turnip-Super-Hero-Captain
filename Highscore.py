__author__ = 'Polle'
import time
import csv
import CsvHandler
class Highscore:
    UserName = ""
    Score = 0
    TimeStamp = 0
    def __init__(self, user, score, timestamp = "bla"):
        self.UserName = user
        self.Score = score
        if timestamp == "bla":
            self.TimeStamp = time.strftime("%x")
        else:
            self.TimeStamp = timestamp
    def __str__(self):
        st = str(self.Score) + " - " + self.UserName + " - " + self.TimeStamp
        return st

    def save(self):
        with open('highscores.csv', 'a+', newline='') as csvfile:
            winnaars = csv.writer(csvfile, delimiter=";")
            winnaars.writerow([self.TimeStamp, self.Score, self.UserName])

def loadHighscore(sortType = "None"):
    f = open('highscores.csv', 'r')
    file = csv.reader(f)
    highscore_list = []
    for row in file:
        row_list = CsvHandler.split(row[0], ";")
        scoreDing = Highscore(row_list[2], row_list[1], row_list[0])
        highscore_list.append(scoreDing)
    return highscore_list

