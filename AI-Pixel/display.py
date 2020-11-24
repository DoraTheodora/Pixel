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
import multiprocessing
from multiprocessing import Process
from multiprocessing import Manager

class GUI:
    root = Tk() ## static variables
    def __init__(self,response):
        self.response = response
        ## Time Displayed
        self.time1 = ''
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S")
        self.clock_frame = tk.Label(GUI.root, font=('Helvica', 75), bg='black', fg='white')
        self.clock_frame.pack(anchor=NW, side=LEFT, padx=20, pady=30)

        self.clock = Label(self.clock_frame, text=self.time2, font=('Helvica', 40), fg='white')
        self.clock.pack(anchor=NW, fill=X, padx=45)
        self.clock.configure(background='black')
        self.changeTime()

        ## Greeting Displayed
        self.greeting_frame = tk.Label(GUI.root, font=('Helvica', 20), bg='black', fg='white')
        self.greeting_frame.pack(anchor=W, side=LEFT)

        self.greetingText = skills.greeting()
        self.greeting = Label(self.greeting_frame, text=self.greetingText, font=('Helvica', 20), bg='black', fg='white')
        self.greeting.pack(anchor=W, fill=X, padx=45)
        self.changeLog()
        
    def changeTime(self):
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S")
        self.clock.configure(text=self.time2)
        self.clock_frame.after(200, self.changeTime)

    def changeLog(self):
        self.answer = self.response.value
        self.greeting.configure(text=self.answer)
        self.greeting_frame.after(200, self.changeLog)


def startAIandGUI():
    with Manager() as manager:
        answer = manager.Value('s','Hello Pixel')
        gui = GUI(answer)
        root = gui.root

        assistant = Process(target=start_AI.startAI, args=(answer,))
        assistant.start()

        root.attributes("-fullscreen", True)
        root.configure(background='black')

        root.mainloop()

