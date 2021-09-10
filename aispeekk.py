import os
from tkinter import *
import pyttsx3

root=Tk()
root.title("AI Speakk")
root.geometry("1200x800")




def talk():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate
    s=int(my_entry_speed.get())
    engine.setProperty('rate', s)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[1].id)  # use woman voice

    engine.say(my_entry_string.get())
    engine.runAndWait()
    my_entry_string.delete(0,END)
    my_entry_speed.delete(0, END)





my_entry_string=Entry(root,font=("Helvectica",28))
my_entry_string.pack(pady=20)

my_entry_speed=Entry(root,font=("Helvectica",28))
my_entry_speed.pack(pady=20)

my_button=Button(root,text="Speak",command=talk)
my_button.pack(pady=20)



root.mainloop()

