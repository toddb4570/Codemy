

from tkinter import *
import os

root = Tk()
root.title("Arrows")
root.geometry("300x100")

def key_pressed(event):
	key = event.keysym

	if key == "Up":
		my_label.config(text="Up!")
	elif key == "Down":
		my_label.config(text="Down")
	elif key == "Left":
		my_label.config(text="Left")
	elif key == "Right":
		my_label.config(text="Right")
	elif key == "q":
		root.destroy()

my_label = Label(root,text="press keys. 'q' to exit ...")
my_label.pack(pady=20)

root.focus_set()

#Bind the keyboard
root.bind('<KeyPress>', key_pressed)

root.mainloop()
