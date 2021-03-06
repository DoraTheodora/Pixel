## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import virtual_assistant
import camera
import skill

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
    """[This class is the interface of the system, and the main process of the system]
    """
    root = Tk() 
    ## Dividing the screen in 1 column and 5 rows
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    def __init__(self, user:str, response:str, virtualAssistantStatus:str, understanding:str):
        """[summary]

        :param user: [The user in front of the camera]
        :type user: str
        :param response: [The text displayed on the mirror-surface]
        :type response: str
        :param virtualAssistantStatus: [The status of the virtual assistant: processing, listening, answering, etc]
        :type virtualAssistantStatus: str
        :param understanding: [What is the understanding of the sytem, of what the user said]
        :type understanding: str
        """
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
        self.greeting_text = ""
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
        """[The method updates the time on the display]
        """
        self.time2 = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.configure(text=self.time2)
        self.clock_label.after(200, self.updateTime)

    ## update virtual assistant's response on GUI
    def displayResponse(self):
        """[The method displays on the screen the virtual assistant's response]
        """
        self.answer = self.response.value
        self.AI_Message_label.configure(text=self.answer)
        self.AI_Message_label.after(200, self.displayResponse)

    ## update virtual assistant's status on GUI
    def displayVirtualAssistantStatus(self):
        """[The method displays on the screen the virtual assistant's status: listening, answering, etc]
        """
        self.virtualAssistantStatus_message = self.virtualAssistantStatus.value
        self.AI_processing_label.configure(text=self.virtualAssistantStatus_message)
        self.AI_processing_label.after(200, self.displayVirtualAssistantStatus)

    ## update virtual assistant's understanding
    def displayVirtualAssistantUnderstanding(self):
        """[The method displays on the screen what the virtual assistant understood from what the user said]
        """
        self.understanding_text = self.understanding.value
        self.understanding_label.configure(text=self.understanding_text)
        self.understanding_label.after(200, self.displayVirtualAssistantUnderstanding)
        

    def close(self):
        """[The method closes the interface]
        """
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
        The following variables are shared between the 3 main processes of the system:

            1. camera process

            2. interface process

            3. the virtual assistant process
        

Camera: 
    The camera starts when the system starts, and its purpose is to detect if a person comes in front of the camera, and to calculate the time between the last moment when a face was detected and the current moment in time
        
        :param user: 
            - this variable contains the name of the user, if its registered, or contains the string 'stranger' if the user standing in front of the camera is not registered
        :param delay: 
            - this variable describes the amount of time since the camera did not detect a face
        :param timeFaceFound: 
            - this variable marks the time when a face was detected the last time
        :param faceFound: 
            - the variable is true when a face is detected by the camera, and is false if there is no face detected by the camera
        :param runCamera: 
            - the variable is True if the camera is running from the Camera process, and false if the camera is not running from this particular process
        :param cameraStopped: 
            - the variable is used as double check, for the "runCamera" variable, that ensures that the camera is running or is stopped in the Camera process


Virtual Assistant: 
    The virtual assistant process stops and starts, depending on the idle time calculated by the camera. The idle time represents the time difference in seconds, since the camera lastly detected a face. If the idle time is greater than 20 seconds, the virtual assistant process is destroyed, and if the idle time is less then 20, the virtual assistant process is created (If the virtual assistant process is running, and the idle time is constantly less than 20 seconds, the virtual assistant process runs until the idle time is greater than 20 seconds).
        
        :param answer: 
            - contains the response provided by the virtual assistant to the user's request
        :param virtualAssistantStatus: 
            - contains the virtual assistant status: processing, listening or having an answer
        :param understanding :
            - contains a string that is displayed on the interface, that represents the request that was understood by the system
        :param root: 
            - GUI class instantiated as the main process
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
        runCamera = manager.Value('b', True)
        capture = Process(target=camera.start,args=(user, faceFound, timeFaceFound, delay, runCamera))
        capture.start()
        cameraStopped = manager.Value('b', False)

        ## variables shares between the display and the virtual_assistance
        answer = manager.Value('s','')
        virtualAssistantStatus = manager.Value('s','')
        understanding = manager.Value('s',' ')
        cameraRunning = manager.Value('b', True)
        assistant = Process(target=virtual_assistant.start, args=(user, answer,virtualAssistantStatus, understanding, cameraRunning))

        ## starting the GUI
        AIStarted = False
        initiatedOnce = True
        display = Display(user, answer, virtualAssistantStatus, understanding)
        root = display.root
        root.attributes("-fullscreen", True)
        root.configure(background='black')
        
        while True:
            if cameraRunning.value == False and cameraStopped.value == False:
                runCamera.value = False
                capture.terminate()
                capture.join()
                cameraStopped.value = True
            if cameraRunning.value == True and cameraStopped.value == True:
                runCamera.value = True
                delay.value = 1
                capture = Process(target=camera.start,args=(user, faceFound, timeFaceFound, delay, runCamera))
                capture.start()
                cameraStopped.value = False
            if faceFound.value and not AIStarted and initiatedOnce:
                assistant.start()
                AIStarted = True  
                initiatedOnce = False     
            if faceFound.value and not AIStarted and not initiatedOnce:
                assistant = Process(target=virtual_assistant.start, args=(user, answer,virtualAssistantStatus, understanding, cameraRunning))
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


        

