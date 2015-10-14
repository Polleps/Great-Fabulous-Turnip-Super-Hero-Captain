__author__ = 'Polle'
import csv
import CsvHandler
import random as ran
class Hero:
    """Hero class with hint method"""
    Name = ""
    Hints = []
    usedHints = []
    def __init__(self, name, hints):
        """Hero class constructor"""
        self.Name = name
        self.Hints = hints

    def hint(self):
        """Method that gives a hint specific to this hero."""
        while True:
            hint_number = ran.randint(0,2)
            if len(self.usedHints) == 3:
                return "No more hints for you!"
            if not hint_number in self.usedHints:
                break

        self.usedHints.append(hint_number)
        return self.Hints[hint_number]
    def __str__(self):
        """To string method"""
        return self.Name
    def getName(self):
        return self.Name

def loadHeroes():
    """Function that loads the heroes from a csv file into a list"""
    hero_list = []
    f = open('marvel.csv')
    marvelFile = csv.reader(f)
    for line in marvelFile:
        marvel_list = CsvHandler.split(line[0], ";")
        hero_list.append(Hero(marvel_list[0], [marvel_list[1], marvel_list[2], marvel_list[3]]))
    return hero_list