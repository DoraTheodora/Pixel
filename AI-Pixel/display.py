## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import virtual_assistant
import camera

import skills
import datetime
import tkinter as tk
import os
import multiprocessing

from tkinter import *
from newsapi import NewsApiClient
from multiprocessing import Process
from multiprocessing import Manager
from PIL import Image, ImageTk

class Display:
    """ The  Display class defines the virtual assistant's graphical interface
        Mirror - Display
    """
    root = Tk() 
    ## Dividing the screen in 1 column and 5 rows
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    def __init__(self, response, virtualAssistantStatus):
        self.response = response
        self.virtualAssistantStatus = virtualAssistantStatus
        #self.video_source = 0

        ## Time Displayed
        self.time1 = ''
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock = Label(self.root, text=self.time2, font=('Helvica', 40), fg='white')
        self.clock.configure(background='black')
        self.clock.grid(row=0, column=0, padx=45, pady=30, sticky=W)
        self.updateTime()

        ## AI Processing Message
        self.AI_processing_message = "Pixel started"
        self.AI_processing = Label(self.root, justify=LEFT ,text = self.AI_processing_message, font=("Helvica", 20), bg="black", fg="white")
        self.AI_processing.grid(row=0, column=3, padx=10, sticky=E)
        self.displayVirtualAssistantStatus()
        
        ## Virtual Assistant Response Displayed
        self.greetingText = skills.greeting()
        self.AI_Message = Label(self.root, justify=LEFT, text=self.greetingText, font=('System', 25), bg='black', fg='white')
        self.AI_Message.grid(row=4, column=0, padx=45, pady=30, sticky=W)
        self.displayResponse()

        ## Camera
        #self.video = camera.Camera(self.video_source)
        #self.video_frame = Canvas(self.root, width=self.video.width, height=self.video.height)
        #self.video_frame.grid(row=2, column=0, padx=45, pady=30, sticky=W)
        #self.updatedCameraFrame()

    ## update time on GUI
    def updateTime(self):
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock.configure(text=self.time2)
        self.clock.after(200, self.updateTime)

    ## update virtual assistant's reponse on GUI
    def displayResponse(self):
        self.answer = self.response.value
        self.AI_Message.configure(text=self.answer)
        self.AI_Message.after(200, self.displayResponse)

    ## update virtual assistant's status on GUI
    def displayVirtualAssistantStatus(self):
        self.virtualAssistantStatus_message = self.virtualAssistantStatus.value
        self.AI_processing.configure(text=self.virtualAssistantStatus_message)
        self.AI_processing.after(200, self.displayVirtualAssistantStatus)

    def close(self):
        self.root.destroy()

    '''
    def updatedCameraFrame(self):
        ret, frame = self.video.getFrame()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.video_frame.create_image(0,0, image = self.photo)
        self.video_frame.after(15, self.updatedCameraFrame) '''

def start():
    """ Provisional main of the program """
    with Manager() as manager:
        faceFound = manager.Value('b', False)
        capture = Process(target=camera.start,args=(faceFound,))
        capture.start()

        answer = manager.Value('s','')
        virtualAssistantStatus = manager.Value('s', '')
        display = Display(answer, virtualAssistantStatus)
        root = display.root
        AIStarted = False

        while True:
            if faceFound.value and not AIStarted:
                root.attributes("-fullscreen", True)
                root.configure(background='black')
                assistant = Process(target=virtual_assistant.start, args=(answer,virtualAssistantStatus))
                assistant.start()
                AIStarted = True
            if faceFound.value and AIStarted:
                root.update()
                

        #root.mainloop()


        

