__author__ = 'Polle'
import csv
import random as ran
import  time
import Highscore
import Hero
import Score

import Timer

score = Score.Score()
name = input("wat is you naam?! ")
score.startGame()
Timer.startTimer(score)
print("Hint 1:")
hero_list = Hero.loadHeroes()
ran.seed(time.gmtime())
random_hero = hero_list[ran.randint(0, len(hero_list) - 1)]
#print(random_hero)
print(random_hero.hint())
while score.GAMESTATE == "STARTED":
    userInput = input("Guess: ")
    if userInput == "hint":
        print(random_hero.hint())
        score.aftrek(3)
    elif userInput == random_hero.getName():
        score.winGame(score, name)
    else:
        score.aftrek(1)
print("The Hero was: ")
print(random_hero)