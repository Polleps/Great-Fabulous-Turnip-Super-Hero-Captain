__author__ = 'Brent'

''' tk_animate_GIF_sequence.py
play a sequence of gifs to create an animation effect
the gif sequence was create with PIL_animatedGif_frames.py
note:  Tkinter cannot display animated gifs directly
(dns)
'''


import itertools as it

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

class Gif():

    def __init__(self):
        self.LoadingScreen = tk.Tk()
        self.label = tk.Label(self.LoadingScreen)
        self.label.pack(padx=10, pady=10)  # store as tk img_objects
        self.fname_list = \
        ['image/A_marvel01.gif',
         'image/A_marvel02.gif',
         'image/A_marvel03.gif',
         'image/A_marvel04.gif',
         'image/A_marvel05.gif',
         'image/A_marvel06.gif',
         'image/A_marvel07.gif',
         'image/A_marvel08.gif',
         'image/A_marvel09.gif',
         'image/A_marvel10.gif',
         'image/A_marvel11.gif',
         'image/A_marvel12.gif',
         'image/A_marvel13.gif',
         'image/A_marvel14.gif',
         'image/A_marvel15.gif',
         'image/A_marvel16.gif',
         'image/A_marvel17.gif',
         'image/A_marvel18.gif']
        self.pictures = it.cycle(tk.PhotoImage(file=img_name) for img_name in self.fname_list)
        # milliseconds
        self.delay = 80
        self.animate()

    def showgif(self):
        self.LoadingScreen.mainloop()

    def animate(self):
        """ cycle through """
        img = next(self.pictures)
        if str(img) == "pyimage18":
            self.LoadingScreen.destroy()
        else:
            self.label["image"] = img
            self.LoadingScreen.after(self.delay, self.animate)



