import os

from gpiozero import LED, Button
from signal import pause
from time import sleep
import pygame


green = LED(17)

for i in range(3):

    for i in range(10):

        green.on()
        sleep(1)
        green.off()
        sleep(1)

pygame.mixer.init()

print("Mixer init...")
curr_index = 0

wav_files = []

# ASSUMING YOU HAVE A DRIVE MOUNTED AT THE FOLLOWING LOCATION
USB_DRIVE = '/media/pi/U/'

for item in os.listdir(USB_DRIVE):

	ext = item[-4:]

        first_two_char = item[:2]

	if ext == ".wav" and first_two_char != "._":

		wav_files.append(USB_DRIVE + item)

for _file in wav_files:

	print("Loaded " + _file)

button = Button(2)

print("Switch initiated")


				
def handle_button():

        green.on()
        sleep(1)
        green.off()

	global curr_index
	
	print("Received button press.")

	if not pygame.mixer.music.get_busy():

		print("Able to initate playback of next track.")

		print("Loading " + wav_files[curr_index])

		pygame.mixer.music.load(wav_files[curr_index])

		print("File Loaded")

		pygame.mixer.music.play()

		print("Playback started.")

		curr_index += 1

		curr_index %= len(wav_files)

		print("Incremetned index, currently " + str(curr_index))


	else:

		print("Cannot initiate playback, system busy.")



button.when_pressed = handle_button

pause()
