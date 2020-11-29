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
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    def __init__(self, response, AIstatus):
        self.response = response
        self.AIstatus = AIstatus
        ## Time Displayed
        self.time1 = ''
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock = Label(self.root, text=self.time2, font=('Helvica', 40), fg='white')
        self.clock.configure(background='black')
        self.clock.grid(row=0, column=0, padx=45, pady=30, sticky=W)
        self.changeTime()

        ## AI Processing Message
        self.AI_processing_message = "Pixel started"
        self.AI_processing = Label(self.root, text = self.AI_processing_message, font=("Helvica", 20), bg="black", fg="white")
        self.AI_processing.grid(row=0, column=3, padx=10, sticky=E)
        self.changeAIProcessing()
        
        ## Greeting Displayed
        self.greetingText = skills.greeting()
        self.AI_Message = Label(self.root, text=self.greetingText, font=('Helvica', 30), bg='black', fg='white')
        self.AI_Message.grid(row=1, column=0, padx=45, pady=30, sticky=W)
        self.changeAIMessage()

    def changeTime(self):
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock.configure(text=self.time2)
        self.clock.after(200, self.changeTime)

    def changeAIMessage(self):
        self.answer = self.response.value
        self.AI_Message.configure(text=self.answer)
        self.AI_Message.after(200, self.changeAIMessage)

    def changeAIProcessing(self):
        self.AIstatus_message = self.AIstatus.value
        self.AI_processing.configure(text=self.AIstatus_message)
        self.AI_processing.after(200, self.changeAIProcessing)

def startAIandGUI():
    with Manager() as manager:
        answer = manager.Value('s','Hello Pixel')
        AIstatus = manager.Value('s', 'Pixel started')
        gui = GUI(answer, AIstatus)
        root = gui.root

        assistant = Process(target=start_AI.startAI, args=(answer,AIstatus))
        assistant.start()

        root.attributes("-fullscreen", True)
        root.configure(background='black')

        root.mainloop()

