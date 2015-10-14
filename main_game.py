__author__ = 'Polle'
import math
import time
import random as ran
def hint(hNumber):
    """"Function die de hints op het scherm gaat zetten (WIP)"""
    hints = ["Het is een marvel character :p", "Hij is groen", "Banner", "Het is een superheld"]
    print(hints[hNumber])

hero_list = ["spiderman", "The Hulk", "Thor", "Iron man"]

ran.seed(time.gmtime())
random_hero = ran.sample(hero_list, 1)
print(random_hero)                                          #ANTWOORD!!!!
print("Eerste Hint:")
hint(0)




