__author__ = 'Brent'

import csv
import operator
import CsvHandler
import time

bestand = open('highscores.csv', 'r')

reader = csv.reader(bestand, delimiter=";")

sort = sorted(reader, key=operator.itemgetter(1), reverse=True)

datum = time.strftime("%x")
maand = CsvHandler.split(time.strftime("%x"),"/")
maand = maand[0]

open("sortedlist.csv", 'w')

for eachline in sort:
    # print(eachline)
    with open("sortedlist.csv", 'a', newline='') as csvfile:
        bla = csv.writer(csvfile, delimiter=';')
        bla.writerow([eachline[0], eachline[1], eachline[2], eachline[3], eachline[4], eachline[5], eachline[6]])

def daily():
    file = open("highscores.csv", 'r')
    lezer = csv.reader(file, delimiter=';')
    surt = sorted(lezer, key=operator.itemgetter(5), reverse=False)
    surt = sorted(surt, key=operator.itemgetter(1), reverse=True)
    open('daily.csv', 'w')
    for elkelijn in surt:
        if elkelijn[0] == datum:
            with open('daily.csv', 'a', newline='') as csvfile:
                blu = csv.writer(csvfile, delimiter=";")
                blu.writerow([elkelijn[0], elkelijn[1], elkelijn[2], elkelijn[3], elkelijn[4], elkelijn[5], elkelijn[6]])

def monthly():
    file = open("highscores.csv", 'r')
    lezer = csv.reader(file, delimiter=';')
    surt = sorted(lezer, key=operator.itemgetter(4), reverse=False)
    surt = sorted(surt, key=operator.itemgetter(1), reverse=True)
    open('monthly.csv', 'w')
    for elkelijn in surt:
        if elkelijn[4] == maand:
            with open('monthly.csv', 'a', newline='') as csvfile:
                blu = csv.writer(csvfile, delimiter=";")
                blu.writerow([elkelijn[0], elkelijn[1], elkelijn[2], elkelijn[3], elkelijn[4], elkelijn[5], elkelijn[6]])



