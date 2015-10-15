__author__ = 'Brent'

import tkinter as tk
from tkinter import *
import gifPlayer

LARGE_FONT= ("Verdana", 12)

class SWGapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoadingScreen, StartPage, StartGame, InsertName, HighScore, HowTo, Exit):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoadingScreen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoadingScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="fack!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Let's play!",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="welkom bij Super Wonder Game the Game!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Let's play!",
                            command=lambda: controller.show_frame(InsertName))
        button.pack()

        button2 = tk.Button(self, text="HighScore?",
                            command=lambda: controller.show_frame(HighScore))
        button2.pack()

        button3 = tk.Button(self, text="How to play",
                            command=lambda: controller.show_frame(HowTo))
        button3.pack()

        button3 = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(Exit))
        button3.pack()

class InsertName(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Insert name:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        entry = Entry(self)
        entry.pack()



class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Let's play: SuperWonderCaptain", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1=tk.Label(self,text="")

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self,text="Hint",
                            command=lambda: controller.show_frame())
        button2.pack()





class HighScore(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HighScore!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Let's Play!!!",
                            command=lambda: controller.show_frame(StartGame))
        button2.pack()

class HowTo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label= tk.Label(self, text="How to play:",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        labelRule=tk.Label(self, text="You start with 25 points and you try to guess the right character to the given description. "+"\n"
                                      "You'll lose points by the following:"+"\n"
                                      "Asking for a hint= -2 point"+"\n"
                                      "Guessing the wrong Character= -1 point"+"\n"
                                      "Every 10 seconds= -1 point"+"\n")
        labelRule.pack(pady=10,padx=0)

        button1 = tk.Button(self,text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self,text="Let's play",
                            command=lambda: controller.show_frame(StartGame))
        button2.pack()

class Exit(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label= tk.Label(self,text="Exit",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2= tk.Button(self,text="Exit",
                           command=closeWindow)
        button2.pack()
def closeWindow():
      app.destroy()

gif = gifPlayer.Gif()
gif.showgif()
app = SWGapp()
app.title("SuperWonderCaptain")
app.mainloop()