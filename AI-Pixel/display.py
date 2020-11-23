## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import start_AI
import skills
import tkinter as tk
from tkinter import *
import datetime
from newsapi import NewsApiClient
import os

root = Tk()

class ClockShow:
    def __init__(self):
        ## Time Displayed
        self.time1 = ''
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S")
        self.clock_frame = tk.Label(root, font=('Helvica', 75), bg='black', fg='white')
        self.clock_frame.pack(anchor=NW, side=LEFT, padx=20, pady=30)

        self.clock = Label(self.clock_frame, text=self.time2, font=('Helvica', 40), fg='white')
        self.clock.pack(anchor=NW, fill=X, padx=45)
        self.clock.configure(background='black')
        self.changeLabel()


    def changeLabel(self):
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S")
        self.clock.configure(text=self.time2)
        self.clock_frame.after(200, self.changeLabel)

 
   
obj = ClockShow()

## greeting displayed
greeting_frame = tk.Label(root, font=('Helvica', 20), bg='black', fg='white')
greeting_frame.pack(anchor=W, side=LEFT)

greetingText = skills.greeting()
greeting = Label(greeting_frame, text=greetingText, font=('Helvica', 20), bg='black', fg='white')
greeting.pack(anchor=W, fill=X, padx=45)


root.attributes("-fullscreen", True)
root.configure(background='black')

root.mainloop()