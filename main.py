import tkinter as tk
import time
import classes 
import win32api
from threading import Thread

def mouseClicked(iLoopLocal,swLocal):
    if (iLoopLocal % 2)== 0:
        swLocal.Start()
    else:  
        swLocal.Stop()
    iLoopIncrement()

def iLoopIncrement():
    # nonlocal iLoop
    global iLoop
    iLoop+=1
    return iLoop
    
iLoop=0

root = tk.Tk() # initializing the tcl/tk interpreter and creating the root window
sw = classes.StopWatch(root)
sw.pack(side=tk.TOP)# Tkinter Pack Geometry Manager

# ----------------------


CurrentKeyState = win32api.GetKeyState(0x04)  # "0x04" is the Virtual-Key Code of the Middle mouse button (VK_MBUTTON)


def firstFunction():
    while True:
        NewKeyState = win32api.GetKeyState(0x04)
        global CurrentKeyState
        if NewKeyState != CurrentKeyState:  # Button state changed

            if NewKeyState < 0:  # KeyState = -127 or -128
                print('BUTTON PRESSED ---', 'NewKeyState = ', NewKeyState )

            else:                # KeyState =1 or 0
                print('BUTTON RELEASED ---', 'NewKeyState = ', NewKeyState)
                mouseClicked(iLoop,sw)
            CurrentKeyState = NewKeyState
            
        time.sleep(0.001)
    
thread1  = Thread(target = firstFunction)
thread1.start()
# root.after(1, firstFunction()) 

root.mainloop() #This method will loop forever, waiting for events from the user, until it exits the program
