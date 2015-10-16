__author__ = 'Polle'
import time
import csv
import CsvHandler
class Highscore:
    UserName = ""
    Score = 0
    TimeStamp = 0
    Seconds = 0
    def __init__(self, user, score, sec, timestamp = "bla"):
        self.UserName = user
        self.Score = score
        self.Seconds = sec
        if timestamp == "bla":
            self.TimeStamp = time.strftime("%x")
        else:
            self.TimeStamp = timestamp
    def __str__(self):
        st = str(self.Score) + " - " + self.UserName + " - " + self.TimeStamp + " - " + self.Seconds
        return st

    def save(self):
        dagmaandjaarList = CsvHandler.split(self.TimeStamp, "/")
        stScore = str(self.Score)
        if(len(stScore) == 1):
            stScore = "0" + stScore
        stSeconds = str(self.Seconds)
        if len(stSeconds) < 4:
            for i in range(4 - len(stSeconds)):
                stSeconds = "0" + stSeconds

        with open('highscores.csv', 'a+', newline='') as csvfile:
            winnaars = csv.writer(csvfile, delimiter=";")
            winnaars.writerow([self.TimeStamp, stScore, self.UserName, stSeconds,dagmaandjaarList[0], dagmaandjaarList[1], dagmaandjaarList[2]])

def loadHighscore(sortType = "None"):
    f = open('highscores.csv', 'r')
    file = csv.reader(f)
    highscore_list = []
    for row in file:
        row_list = CsvHandler.split(row[0], ";")
        scoreDing = Highscore(row_list[2], row_list[1], row_list[3], row_list[0])
        highscore_list.append(scoreDing)
    return highscore_list

