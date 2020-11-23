## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import threading

import display
import start_AI

def start():
    gui = display.startGUI()
    root = gui.getRoot()

    assistant = threading.Thread(target=start_AI.start, args=())
    assistant.start()

    root.attributes("-fullscreen", True)
    root.configure(background='black')

    root.mainloop()

start()
