from curses import beep
import screeninfo
import tkinter as tk
from tkinter import *
import argparse
import simpleaudio
from mutagen.mp3 import MP3
import numpy as np
import os
import random
import vlc
from pygame import mixer

time = 0


def playBeep():
    wave_obj = simpleaudio.WaveObject.from_wave_file("assets/beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def getMP3Duration(file_path):
    audio = MP3(file_path)
    return int(np.ceil(audio.info.length))*1000

# Configure CLI parser early. This way we don't need to load TF if there's a missing arg.
parser = argparse.ArgumentParser(
    description='Synthoice!', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

screen_choices = []
for i in range(len(screeninfo.get_monitors())):
    screen_choices.append(i+1)
# TO-DO
parser.add_argument('--screen', default=1, type=int, choices=screen_choices,
                    help='The screen number for displaying the expriment')

args = parser.parse_args()


root = tk.Tk()
root.bind("<Escape>", lambda x: root.destroy())


root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)

root.update()

# Get the width
width = root.winfo_width()
# Get the height
height = root.winfo_height()
print("Width: ", width)   # Display the width
print("Height: ", height)  # Display the height

main_canvas = Canvas(root, width=width, height=height, background="lightgray")
main_canvas.pack()
main_canvas.update()

main_canvas.create_text(int(width/2), int(height/2), fill="black",
                        font="Times 60 italic bold", text="+")

def black():
    main_canvas.create_text(int(width/2), int(height/2), fill="black",
                        font="Times 60 italic bold", text="+")

def red():
    main_canvas.create_text(int(width/2), int(height/2), fill="red",
                        font="Times 60 italic bold", text="+")


materials_dir = "materials"
all_files = os.listdir(materials_dir)
random.shuffle(all_files)

voices = []
durations = []
for i in range(len(all_files)):
    if all_files[i].endswith(".mp3"):
        voices.append(materials_dir + "/" + all_files[i].split(".mp3")[0] + ".wav")
        durations.append(getMP3Duration(materials_dir + "/" + all_files[i]))






root.after(time + 2000, playBeep)
time = time + 2000

current_file = "materials/1.wav"

def play_voice():
    wave_obj = simpleaudio.WaveObject.from_wave_file(current_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

for i in range(len(voices)):
    root.after(time+50, red)
    dur = durations[i]
    current_file = voices[i]
    root.after(time, play_voice)
    root.after(time + dur, black)
    time = time + dur


root.mainloop()
