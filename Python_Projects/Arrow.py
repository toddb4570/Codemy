
from pynput import keyboard
import os

os.system("clear")

def on_press(key):
	print (key)

	try:
		if key.char == 'q':
			return False

	except AttributeError:
		pass

	if key == keyboard.Key.up:
		print("Up")
	elif key == keyboard.Key.down:
		print("Down")
	elif key == keyboard.Key.left:
		print("Left")
	elif key == keyboard.Key.right:
		print("Right")

print("press keys. 'q' to exit: ")


# create and a keyboard listener
with keyboard.Listener(on_press=on_press)  as listener: # create the listener object
	listener.join() # start listener
