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
import time

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
    """ 
        The provisional main of the program
         
        :param delay: is a shared variable between the camera process and interface 
            - this variable describes the amount of time since the camera did not detect a face
        :param timeFaceFound: is a shared variable between the camera process and the interface
            - this variable marks the time when a face was detected the last time
        :param faceFound: is a shared boolean variable between the camera process and the interface
            - the variable is true when a face is detected by the camera, and is false if there is no face detected by the camera
        :param camera: is the camera class instantiated as a process
        :param answer: is a shared variable between the virtual assistant and the interface
            - contains the response provided by the virtual assistant to the user's request
        :param virtualAssistantStatus: is a variable shared between the virtual assistant and the interface
            - contains the virtual assistant status: processing, listening or having an answer
        :param root: is the GUI class instantiated as the main process
        :param AIStarted: is a boolean variable that reflects the virtual_assistant status
            - true if the virtual assistant status is running
            - false if the virtual assistant is not running
            - used like a semaphore, not allowing the instantiation of the virtual_assistant multiple times if the virtual assistant runs already
    """
    with Manager() as manager:
        ## variables shared between the camera and the display  
        delay = manager.Value('f', 0)
        timeFaceFound = manager.Value('f', time.time())
        faceFound = manager.Value('b', False)
        capture = Process(target=camera.start,args=(faceFound,timeFaceFound, delay))
        capture.start()

        ## variables shares between the display and the virtual_assistance
        answer = manager.Value('s','')
        virtualAssistantStatus = manager.Value('s', '')
        display = Display(answer, virtualAssistantStatus)
        root = display.root

        ## starting the GUI
        AIStarted = False
        initiatedOnce = True
        assistant = Process(target=virtual_assistant.start, args=(answer,virtualAssistantStatus))
        root.attributes("-fullscreen", True)
        root.configure(background='black')
        while True:
            if faceFound.value and not AIStarted and initiatedOnce:
                assistant.start()
                AIStarted = True  
                initiatedOnce = False     
            if faceFound.value and not AIStarted and not initiatedOnce:
                assistant = Process(target=virtual_assistant.start, args=(answer,virtualAssistantStatus))
                assistant.start()
                AIStarted = True 
            if delay.value > 5 and AIStarted:
                assistant.terminate()
                assistant.join()
                answer.value = ""
                virtualAssistantStatus.value = ""
                AIStarted = False
                #print("Idle time: ", delay.value)
            root.update()
        #root.mainloop()


        

