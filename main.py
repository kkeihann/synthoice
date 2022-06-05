from curses import beep
import screeninfo
import tkinter as tk
from tkinter import *
import argparse
import simpleaudio 

time = 0

def playBeep():
    wave_obj = simpleaudio.WaveObject.from_wave_file("assets/beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

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

main_canvas.create_text(int(width/2), int(height/2), fill="red",
                        font="Times 60 italic bold", text="+")


root.after(time + 2000, playBeep)
time = time + 2000

root.after(time + 2000, playBeep)
time = time + 2000


root.mainloop()
