import tkinter as tk
import pyttsx3


count=0

def countplus():
    global count
    count=count+1

root = tk.Tk()
root.geometry('600x400')
root.title("AI Speak")


def talk00():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate

    engine.setProperty('rate', 100)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[0].id)  # use woman voice

    engine.say(my_entry_string.get())
    global count

    engine.save_to_file(my_entry_string.get(), 'No.'+str(count)+' result(Text to Speech).mp3')
    countplus()
    engine.runAndWait()




def talk01():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate

    engine.setProperty('rate', 100)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[1].id)  # use woman voice

    engine.say(my_entry_string.get())
    global count

    engine.save_to_file(my_entry_string.get(), 'No.' + str(count) + ' result(Text to Speech).mp3')
    countplus()
    engine.runAndWait()


def talk10():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate

    engine.setProperty('rate', 200)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[0].id)  # use woman voice

    engine.say(my_entry_string.get())
    global count

    engine.save_to_file(my_entry_string.get(), 'No.' + str(count) + ' result(Text to Speech).mp3')
    countplus()
    engine.runAndWait()


def talk11():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate

    engine.setProperty('rate', 200)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[1].id)  # use woman voice

    engine.say(my_entry_string.get())
    global count

    engine.save_to_file(my_entry_string.get(), 'No.' + str(count) + ' result(Text to Speech).mp3')
    countplus()
    engine.runAndWait()

def talk20():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate

    engine.setProperty('rate', 300)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[0].id)  # use woman voice

    engine.say(my_entry_string.get())
    global count

    engine.save_to_file(my_entry_string.get(), 'No.' + str(count) + ' result(Text to Speech).mp3')
    countplus()
    engine.runAndWait()


def talk21():
    engine = pyttsx3.init()  # initiate engine

    rate = engine.getProperty('rate')  # get the rate

    engine.setProperty('rate', 200)  # set the rate

    voices = engine.getProperty('voices')  # get the details of engine
    engine.setProperty('voice', voices[1].id)  # use woman voice

    engine.say(my_entry_string.get())
    global count

    engine.save_to_file(my_entry_string.get(), 'No.' + str(count) + ' result(Text to Speech).mp3')
    countplus()
    engine.runAndWait()

"Menu Design"

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="Slow Speed Male Voice",command=talk00)

filemenu.add_command(label="Slow Speed Female Voice",command=talk01)

filemenu.add_command(label="Normal Speed Male Voice",command=talk10)

filemenu.add_command(label="Normal Speed Female Voice",command=talk11)

filemenu.add_command(label="Fast Speed Male Voice",command=talk20)

filemenu.add_command(label="Fast Speed Female Voice",command=talk21)
menubar.add_cascade(label="Text To Speech", menu=filemenu)



filemenu4 = tk.Menu(menubar,tearoff=0)
filemenu4.add_command(label="Xuchen Sun")
filemenu4.add_command(label="Email: xuchens@mun.ca")
filemenu4.add_command(label="Phone: 7092190068")
menubar.add_cascade(label="Author", menu=filemenu4)




root.config(menu=menubar)




my_entry_string=tk.Entry(root,font=("Helvectica",28))
my_entry_string.pack(pady=20)


















root.mainloop()