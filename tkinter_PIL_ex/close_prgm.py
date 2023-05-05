import subprocess
import time
import psutil
import os
import random
import tkinter

from tkinter import *
from tkinter import messagebox


def checkProgram():
    for i in psutil.process_iter():
        print(i.name())
    if "Google Chrome" in (i.name() for i in psutil.process_iter()):
        return True


def killProgram():
    for proc in psutil.process_iter():
        if proc.name() == "Google Chrome":
            os.kill(proc.pid, 9)
    errormessage = "error message"
    messagebox.showwarning(title="Test", message=errormessage)
    root.destroy()


root = Tk()
root.withdraw()

while True:
    if checkProgram():
        killProgram()
    time.sleep(5)


