__author__ = 'Polle'
import time
import math
import threading as thread
import Score

def timer(score):
    t = math.floor(time.clock())
    turnip_tijd = t
    while score.GAMESTATE == "STARTED":
        old_time = t
        if t > turnip_tijd + 9:
            turnip_tijd = t
            print("Punt aftrek!")       #punt aftrek functie aanroepen
            score.aftrek(2)
        t = math.floor(time.clock())
        if t > old_time:
            #print(t)
            pass


def startTimer(score):
    try:
        threadje = thread.Thread(target=timer, args=(score,))
        threadje.start()
    except Exception as error_info:
        print(error_info)

