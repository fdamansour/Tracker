import tkinter as tk
import time
import classes 
# from functions import *

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

frame = tk.Frame(root, width=100, height=100)
frame.bind("<Button-2>", lambda x=None: mouseClicked(iLoop,sw)) #bind Python functions and methods to events
frame.pack() # Tkinter Pack Geometry Manager

root.mainloop() #This method will loop forever, waiting for events from the user, until it exits the program
    
    
