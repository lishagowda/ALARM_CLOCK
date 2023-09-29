from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
from threading import Thread
from pygame import mixer

mixer.init()

# Function to activate the alarm
def activate_alarm():
    global is_alarm_activated
    is_alarm_activated = True
    rad1.configure(text="Activated")
    rad2.configure(text="Deactivate")
    t = Thread(target=alarm)
    t.start()

# Function to deactivate the alarm
def deactivate_alarm():
    global is_alarm_activated
    is_alarm_activated = False
    rad1.configure(text="Activate")
    rad2.configure(text="Deactivate")

# Function to change the Radiobutton text to "Deactivate"
def change_to_deactivate():
    rad1.configure(text="Activated")
    rad2.configure(text="Deactivate")

# Function to change the Radiobutton text to "Activate"
def change_to_activate():
    rad1.configure(text="Activate")
    rad2.configure(text="Deactivate")

# Function to play the alarm sound
def sound_alarm():
    mixer.music.load('Alarm.mp3')  # Update with your alarm sound file
    mixer.music.play()
    selected.set(0)

# Function to handle the alarm logic
def alarm():
    while True:
        control = selected.get()

        alarm_hour = clock_hour.get()
        alarm_minute = clock_min.get()
        alarm_sec = clock_sec.get()
        alarm_period = clock_period.get().upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break!")
                            sound_alarm()

        sleep(1)

# Writing code for Windows
window = Tk()
window.title("Alarm Clock with GUI")
window.geometry('720x360')
window.configure(bg="black")

# Frames
frame1 = Frame(window, width=500, height=10, bg="black")
frame1.grid(row=0, column=0)

frame2 = Frame(window, width=500, height=200, bg="black")
frame2.grid(row=1, column=0)

# Configuring Frame Body
img = Image.open('Clock.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame2, height=150, image=img, bg="black")
app_image.place(x=10, y=10)

name = Label(frame2, text="Alarm Clock", height=1, font="Ivy 20 bold", bg="black", fg="white")
name.place(x=130, y=15)

# Creating Hour Part of Clock
hour = Label(frame2, text="Hour", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
hour.place(x=128, y=60)

# Creating Dropbox for Hour (Combobox)
clock_hour = Combobox(frame2, width=2, font='arial 15', height=10)
clock_hour['values'] = tuple(f"{i:02}" for i in range(13))
clock_hour.current(0)
clock_hour.place(x=130, y=90)

# Creating Minute Part of Clock
min = Label(frame2, text="Min", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
min.place(x=180, y=60)

# Creating Dropbox for Minutes (Combobox)
clock_min = Combobox(frame2, width=2, font='arial 15')
clock_min['values'] = tuple(f"{i:02}" for i in range(60))
clock_min.current(0)
clock_min.place(x=180, y=90)

# Creating Seconds Part of Clock
sec = Label(frame2, text="Sec", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
sec.place(x=230, y=60)

# Creating Dropbox for Seconds (Combobox)
clock_sec = Combobox(frame2, width=2, font='arial 15')
clock_sec['values'] = tuple(f"{i:02}" for i in range(60))
clock_sec.current(0)
clock_sec.place(x=230, y=90)

# Creating Period Part of Clock
period = Label(frame2, text="Period", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
period.place(x=280, y=60)

# Creating Dropbox for Period (Combobox)
clock_period = Combobox(frame2, width=3, font='arial 15')
clock_period['values'] = ("AM", "PM")
clock_period.current(0)
clock_period.place(x=280, y=90)

# Initialize variables and GUI components
now = datetime.now()
selected = IntVar()
is_alarm_activated = False

rad1 = Radiobutton(frame2, font="arial 11 bold", value=1, text="Activate", bg="black", fg="white", command=lambda: [activate_alarm(), change_to_deactivate()], variable=selected)
rad1.place(x=130, y=140)
rad2 = Radiobutton(frame2, font="arial 11 bold", value=2, text="Deactivate", bg="black", fg="white", command=lambda: [deactivate_alarm(), change_to_activate()], variable=selected)
rad2.place(x=250, y=140)

# Create a label to display the clock
clock_label = Label(frame2, text="", font="Ivy 15", bg="black", fg="white")
clock_label.place(x=10, y=170)

# Function to update the clock label with the current time
def update_clock_label():
    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")  # 12-hour time format with AM/PM
        clock_label.config(text=current_time)
        sleep(1)  # Update every second

# Start a thread to update the clock label
clock_thread = Thread(target=update_clock_label)
clock_thread.daemon = True  # Daemonize the thread to stop it when the main program ends
clock_thread.start()

mixer.init()

window.mainloop()
