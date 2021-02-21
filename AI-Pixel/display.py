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
    """[summary]
    """
    root = Tk() 
    ## Dividing the screen in 1 column and 5 rows
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    def __init__(self, user:str, response:str, virtualAssistantStatus:str, understanding:str):
        self.response = response
        self.virtualAssistantStatus = virtualAssistantStatus
        self.understanding = understanding
        #self.video_source = 0

        ## Time Displayed
        self.time1 = ''
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock_label = Label(self.root, text=self.time2, font=('Helvica', 45), fg='white')
        self.clock_label.configure(background='black')
        self.clock_label.grid(row=0, column=0, padx=1, pady=30, sticky=W)
        self.updateTime()

        ## AI Processing Message
        self.AI_processing_message = "Pixel started"
        self.AI_processing_label = Label(self.root, justify=LEFT ,text = self.AI_processing_message, font=("Helvica", 20), bg="black", fg="white")
        self.AI_processing_label.grid(row=0, column=3, padx=1, sticky=E)
        self.displayVirtualAssistantStatus()
        
        ## Virtual assistant understanding
        self.understanding_text = " "
        self.understanding_label = Label(self.root, justify=LEFT, text = self.understanding_text, font=("Helvica", 17), bg="black", fg="yellow" )
        self.understanding_label.grid(row=1, column=0, padx=1,pady=10, sticky=W)
        self.displayVirtualAssistantUnderstanding()    

        ## Virtual Assistant Response Displayed
        self.greeting_text = skills.greeting(user.value)
        self.AI_Message_label = Label(self.root, justify=LEFT, text=self.greeting_text, font=('System', 20), bg='black', fg='white')
        self.AI_Message_label.grid(row=4, column=0, padx=1, pady=30, sticky=W)
        self.displayResponse()

        ## Camera
        #self.video = camera.Camera(self.video_source)
        #self.video_frame = Canvas(self.root, width=self.video.width, height=self.video.height)
        #self.video_frame.grid(row=2, column=0, padx=45, pady=30, sticky=W)
        #self.updatedCameraFrame()

    ## update time on GUI
    def updateTime(self):
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.configure(text=self.time2)
        self.clock_label.after(200, self.updateTime)

    ## update virtual assistant's reponse on GUI
    def displayResponse(self):
        self.answer = self.response.value
        self.AI_Message_label.configure(text=self.answer)
        self.AI_Message_label.after(200, self.displayResponse)

    ## update virtual assistant's status on GUI
    def displayVirtualAssistantStatus(self):
        self.virtualAssistantStatus_message = self.virtualAssistantStatus.value
        self.AI_processing_label.configure(text=self.virtualAssistantStatus_message)
        self.AI_processing_label.after(200, self.displayVirtualAssistantStatus)

    ## update virtual assistant's understanding
    def displayVirtualAssistantUnderstanding(self):
        self.understanding_text = self.understanding.value
        self.understanding_label.configure(text=self.understanding_text)
        self.understanding_label.after(200, self.displayVirtualAssistantUnderstanding)
        

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
        :param timeFaceFound: shared variable between the camera process and the interface
            - this variable marks the time when a face was detected the last time
        :param faceFound: shared boolean variable between the camera process and the interface
            - the variable is true when a face is detected by the camera, and is false if there is no face detected by the camera
        :param camera: camera class instantiated as a process
        :param answer: shared variable between the virtual assistant and the interface
            - contains the response provided by the virtual assistant to the user's request
        :param virtualAssistantStatus: variable shared between the virtual assistant and the interface
            - contains the virtual assistant status: processing, listening or having an answer
        :param root: GUI class instantiated as the main process
        :param AIStarted: boolean variable that reflects the virtual_assistant status
            - true if the virtual assistant status is running
            - false if the virtual assistant is not running
            - used like a semaphore, not allowing the instantiation of the virtual_assistant multiple times if the virtual assistant runs already
    """
    with Manager() as manager:
        ## variables shared between the camera and the display  
        user = manager.Value('s', "stranger")
        delay = manager.Value('f', 0)
        timeFaceFound = manager.Value('f', time.time())
        faceFound = manager.Value('b', False)
        capture = Process(target=camera.start,args=(user, faceFound, timeFaceFound, delay))
        capture.start()
        cameraStopped = manager.Value('b', False)

        ## variables shares between the display and the virtual_assistance
        answer = manager.Value('s','')
        virtualAssistantStatus = manager.Value('s','')
        understanding = manager.Value('s',' ')
        cameraRunning = manager.Value('b', True)
        display = Display(user, answer, virtualAssistantStatus, understanding)
        root = display.root

        ## starting the GUI
        AIStarted = False
        initiatedOnce = True
        assistant = Process(target=virtual_assistant.start, args=(user, answer,virtualAssistantStatus, understanding, cameraRunning, cameraStopped))
        root.attributes("-fullscreen", True)
        root.configure(background='black')
        
        while True:
            if cameraRunning.value == False and cameraStopped.value == False:
                print("[INFO] Main camera stopped")
                capture.terminate()
                capture.join()
                cameraStopped.value = True
            if cameraRunning == True and cameraStopped == True:
                capture = Process(target=camera.start,args=(user, faceFound, timeFaceFound, delay))
                capture.start()
                cameraStopped.value = False
            if faceFound.value and not AIStarted and initiatedOnce:
                assistant.start()
                AIStarted = True  
                initiatedOnce = False     
            if faceFound.value and not AIStarted and not initiatedOnce:
                assistant = Process(target=virtual_assistant.start, args=(user, answer,virtualAssistantStatus, understanding, cameraRunning, cameraStopped))
                assistant.start()
                AIStarted = True 
            if delay.value > 20 and AIStarted:
                assistant.terminate()
                assistant.join()
                answer.value = ""
                virtualAssistantStatus.value = ""
                understanding.value = ""
                AIStarted = False
                #print("Idle time: ", delay.value)
            root.update()
        #root.mainloop()


        

