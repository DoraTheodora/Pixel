## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import virtual_assistant
import skills
import tkinter as tk
from tkinter import *
import datetime
from newsapi import NewsApiClient
import os
import multiprocessing
from multiprocessing import Process
from multiprocessing import Manager
import camera
from PIL import Image, ImageTk

class Display:
    root = Tk() ## static variables
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    def __init__(self, response, virtualAssistantStatus):
        self.response = response
        self.virtualAssistantStatus = virtualAssistantStatus
        self.video_source = 0
        ## Time Displayed
        self.time1 = ''
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock = Label(self.root, text=self.time2, font=('Helvica', 40), fg='white')
        self.clock.configure(background='black')
        self.clock.grid(row=0, column=0, padx=45, pady=30, sticky=W)
        self.updateTime()

        ## AI Processing Message
        self.AI_processing_message = "Pixel started"
        self.AI_processing = Label(self.root, text = self.AI_processing_message, font=("Helvica", 20), bg="black", fg="white")
        self.AI_processing.grid(row=0, column=3, padx=10, sticky=E)
        self.displayVirtualAssistantStatus()
        
        ## Greeting Displayed
        self.greetingText = skills.greeting()
        self.AI_Message = Label(self.root, text=self.greetingText, font=('Helvica', 30), bg='black', fg='white')
        self.AI_Message.grid(row=4, column=0, padx=45, pady=30, sticky=W)
        self.displayResponse()

        ## Camera
        #self.video = camera.Camera(self.video_source)
        #self.video_frame = Canvas(self.root, width=self.video.width, height=self.video.height)
        #self.video_frame.grid(row=2, column=0, padx=45, pady=30, sticky=W)
        #self.updatedCameraFrame()

    def updateTime(self):
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock.configure(text=self.time2)
        self.clock.after(200, self.updateTime)

    def displayResponse(self):
        self.answer = self.response.value
        self.AI_Message.configure(text=self.answer)
        self.AI_Message.after(200, self.displayResponse)

    def displayVirtualAssistantStatus(self):
        self.virtualAssistantStatus_message = self.virtualAssistantStatus.value
        self.AI_processing.configure(text=self.virtualAssistantStatus_message)
        self.AI_processing.after(200, self.displayVirtualAssistantStatus)
    '''
    def updatedCameraFrame(self):
        ret, frame = self.video.getFrame()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.video_frame.create_image(0,0, image = self.photo)
        self.video_frame.after(15, self.updatedCameraFrame) '''

def start():
    with Manager() as manager:
        answer = manager.Value('s','Hello Pixel')
        virtualAssistantStatus = manager.Value('s', 'Pixel started')
        display = Display(answer, virtualAssistantStatus)
        root = display.root

        assistant = Process(target=virtual_assistant.start, args=(answer,virtualAssistantStatus))
        assistant.start()


        root.attributes("-fullscreen", True)
        root.configure(background='black')

        root.mainloop()

