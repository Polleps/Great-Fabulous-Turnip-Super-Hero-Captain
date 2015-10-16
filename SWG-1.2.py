__author__ = 'Turnip'

import tkinter as tk
from tkinter import *
import random as ran
import  time
import Hero
import Score
import gifPlayer
import csv
import CsvHandler
import Timer
import highscore_interpreter
SMALL_FONT = ("Verdana",7)
FONT = ("Arial",11)
LARGE_FONT= ("Verdana", 12)
WINING_FONT=("Comic Sans", 20)
USERNAME = ""
HEIGHT = 400
WIDTH = 550
SCORE = 0
TIME = 0
def ranHero():
    hero_list = Hero.loadHeroes()
    HER0 = hero_list[ran.randint(0, len(hero_list) - 1)]
    return HER0
def newScore():
    SC0RE = Score.Score()
    return SC0RE

SCORE = newScore()
HERO = ranHero()
class SWGapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        global TIMEVAR
        TIMEVAR = StringVar()
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (InsertName, StartPage, StartGame,WinScreen, HighScore, HowTo, Exit):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Super Wonder Captain the Game!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Let's play!",
                            command=lambda: controller.show_frame(InsertName))
        button.pack(fill=X)

        button2 = tk.Button(self, text="HighScore?",
                            command=lambda: controller.show_frame(HighScore))
        button2.pack(fill=X)

        button3 = tk.Button(self, text="How to play",
                            command=lambda: controller.show_frame(HowTo))
        button3.pack(fill=X)

        button3 = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(Exit))
        button3.pack(fill=X)

class InsertName(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Insert name:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        entry = Entry(self)
        entry.pack()

        button = tk.Button(self, text="Enter",
                           command=lambda: toStart(entry.get(), controller))
        button.pack(fill=X)

        button2 = tk.Button(self, text="Return home",
                           command=lambda: controller.show_frame(StartPage))
        button2.pack(fill=X)

def toStart(message, controller):

    if message is not "":
        global TIMEVAR
        controller.show_frame(StartGame)
        global USERNAME
        USERNAME = message

        Timer.startTimer(SCORE,TIMEVAR)

def checkInput(message, score, scVar, controller):
    if message == HERO.getName():
        score.winGame(SCORE,USERNAME)
        win(controller)
    else:
        score.aftrek(1, scVar)

class StartGame(tk.Frame):
    counter=0
    inputBox = 0
    def __init__(self, parent, controller):
        global TIMEVAR

        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Anwser:").grid(row=20,column=1)
        tk.Label(self, text="Hint1:").grid(row=4,column=0)
        tk.Label(self, text="Hint2:").grid(row=6,column=0)
        tk.Label(self, text="Hint3:").grid(row=8,column=0)

        tk.Label(self,text= hintSchrijven(self,HERO.hint())).grid(row=4,column=1) ##Eerste hint##

        tk.Label(self, text="Time:").grid(row=20,column=3)
        tk.Label(self, text="Score:").grid(row=21,column=3)
        scoreVar = StringVar()
        scoreVar.set("25")
        timeLabel = tk.Label(self, textvariable=TIMEVAR)
        scoreLabel =tk.Label(self, textvariable=scoreVar)

        timeLabel.grid(row=20,column=4)
        scoreLabel.grid(row=21,column=4)
        entry1 = Entry(self)
        self.inputBox = entry1
        entry1.grid(row=21, column=1)
        name = entry1.get()

        tk.Button(self,text="Show hint",
                  command=lambda: self.showLabel(tk, SCORE, scoreVar)).grid(row=31,column=1)
        tk.Button(self,text="Guess",
                  command=lambda: checkInput(entry1.get(), SCORE, scoreVar, controller)).grid(row=30,column=1)

        name = USERNAME
        SCORE.startGame()


        ran.seed(time.gmtime())

    def showLabel(self,tk, score, label):
        if self.counter is 0:
            tk.Label(self,text= hintSchrijven(self,HERO.hint())).grid(row=6,column=1)
            score.aftrek(3, label)
        elif self.counter is 1:
            tk.Label(self,text= hintSchrijven(self,HERO.hint())).grid(row=8,column=1)
            score.aftrek(3, label)
        elif self.counter is 3:
            self.counter=0
        self.counter += 1


def hintSchrijven(self, text):
    if text is not "":
       return text




    # def update_clock(self):
    #     now = time.strftime("%M:%S")
    #     self.label.configure(text=now)
    #     self.root.after(1000, self.update_clock)


def win(controller):
    controller.show_frame(WinScreen)
    highscore_interpreter.daily()
    highscore_interpreter.monthly()

class HighScore(tk.Frame):

    def __init__(self, parent, controller):

        scores = StringVar()
        loadScores("sortedlist", scores)

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HighScore!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, textvariable=scores)
        #label = tk.Label(self, text="a\nb\nc\n")
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button3 = tk.Button(self, text="Sort Score", command=lambda: loadScores("sortedlist", scores))
        button3.pack()

        button4 = tk.Button(self, text="Sort Daily", command=lambda: loadScores("daily", scores))
        button4.pack()

        button5 = tk.Button(self, text="Sort Monthly", command=lambda: loadScores("monthly", scores))
        button5.pack()

def loadScores(fileName, sc):
    fileName += ".csv"
    file = open(fileName, "r")
    bestand = csv.reader(file)
    outputString = ""
    count = 1
    for row in bestand:
        punten = CsvHandler.split(row[0], ";")
        outputString = outputString + str(count) + ": " + punten[2] + " - Score: " + punten[1] + " - Date: " + punten[0] + "\n"
        count += 1
    sc.set(outputString)

class HowTo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label= tk.Label(self, text="How to play:",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        labelRule=tk.Label(self, text="You start with 25 points and you try to guess the right character to the given description. "+"\n"
                                      "You'll lose points by the following:"+"\n"
                                      "Asking for a hint= -2 point"+"\n"
                                      "Guessing the wrong Character= -1 point"+"\n"
                                      "Every 10 seconds= -1 point"+"\n",justify = LEFT)
        labelRule.pack(fill=X)

        button1 = tk.Button(self,text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(fill=X)


class WinScreen(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="You fckn did it!",font=WINING_FONT)
        label.pack(side=TOP)

        label2=tk.Label(self,text="The following students worked on this:"+"\n"
                        "Faycal el Ouaret............1677694"+"\n"
                        "Brent Cranko.................1674189"+"\n"
                        "Polle Pas........................1692012"+"\n"
                        "Robin van der Want.....1684509"+"\n"
                        "Tim Hartog....................1677480"+"\n"
                        "Joris Boers.....................1657009"+"\n")
        label2.pack()
        button1=tk.Button(self,text="Exit",
                                  command=lambda: controller.show_frame(Exit))
        button1.pack(side=BOTTOM,fill=X)




class Exit(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Are you sure?",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,text="No",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(fill=X)

        button2= tk.Button(self,text="Yes",
                           command=closeWindow)
        button2.pack(fill=X)
def closeWindow():
    app.destroy()

gif = gifPlayer.Gif()
gif.showgif()

app = SWGapp()
app.title("SuperWonderCaptain")
app.geometry(str(WIDTH) + 'x' + str(HEIGHT))
app.mainloop()