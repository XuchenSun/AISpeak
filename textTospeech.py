
from tkinter import *
import pyttsx3

root=Tk()
root.title("AI Speakk")
root.geometry("1200x800")
root.iconbitmap()

engine=pyttsx3.init()                     # initiate engine


rate = engine.getProperty('rate')  # get the rate
engine.setProperty('rate', 150)     # set the rate


voices = engine.getProperty('voices')      #get the details of engine
engine.setProperty('voice', voices[1].id)    # use woman voice




engine.say("Hello, I am Xuchen")
engine.runAndWait()
root.mainloop()