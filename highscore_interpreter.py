__author__ = 'Brent'

import csv
import operator

bestand = open('highscores.csv', 'r')

reader = csv.reader(bestand, delimiter=";")

sort = sorted(reader, key=operator.itemgetter(1), reverse=True)

open("sortedlist", 'w')

for eachline in sort:
    print(eachline)
    with open("sortedlist", 'a', newline='') as csvfile:
        bla = csv.writer(csvfile, delimiter=';')
        bla.writerow([eachline])

