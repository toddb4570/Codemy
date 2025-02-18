import time
from datetime import datetime
import os
import threading
from zoneinfo import ZoneInfo

def clear_screen():
	os.system("clear")

def input_thread(stop_event):
	input()
	stop_event.set()

def main():

	# Set up time zones
	time_zones = {
	'1':('Eastern Time', 'America/New_York'),
	'2':('Central Time', 'America/Chicago'),
	'3':('Pacific Time', 'America/Los_Angeles')
	}
	print("Select a time zone:")

	#loop through timezones
	for key, (name, _) in time_zones.items():
		print(f"{key}. {name}")

	choice = input("Enter the number of your choice: ").strip()

	if choice not in time_zones:
		print("Invalid choice. Defaulting to Eastern Time.")
		tz_name = "America/New_York"
		tz_Display_name = "Eastern Time"
	else:
		tz_display_name, tz_name =  time_zones[choice]

	# create an event to signal when to stop the clock
	stop_event = threading.Event()

	thread = threading.Thread(target=input_thread, args=(stop_event, ))
	thread.daemon = True
	thread.start()

	while not stop_event.is_set():
		clear_screen()
#		current_time = time.strftime("%H:%M:%S")
		current_time = datetime.now(ZoneInfo(tz_name)).strftime("%H:%M:%S")
		print (f"Current time: {current_time} - {tz_display_name}")
		print ("Press <ENTER> to stop the clock...")
		time.sleep(1)

	print("Clock stopped")

main()