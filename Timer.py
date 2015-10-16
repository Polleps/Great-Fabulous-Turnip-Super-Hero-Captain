__author__ = 'Polle'
import time
import math
import threading as thread
import Score

def timer(score, label):
    t = math.floor(time.clock())
    turnip_tijd = t
    while score.GAMESTATE == "STARTED":
        old_time = t
        if t > turnip_tijd + 9:
            turnip_tijd = t

            score.aftrek(2, label)
        t = math.floor(time.clock())
        if t > old_time:
            #print(t)
            score.Time = t
            label.set(value=str(t))


def startTimer(score, label):
    try:
        threadje = thread.Thread(target=timer, args=(score,label,))
        threadje.start()
    except Exception as error_info:
        #print(error_info)
        pass

