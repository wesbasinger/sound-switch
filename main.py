import os

from gpiozero import LED, Button
from signal import pause
from time import sleep
import pygame

pygame.mixer.init()

print("Mixer init...")

curr_index = 0

wav_files = []

dir_path = os.path.dirname(os.path.realpath(__file__))

for item in os.listdir(dir_path):

	ext = item[-4:]

	if ext == ".wav":

		wav_files.append(item)

for _file in wav_files:

	print("Loaded " + _file)

button = Button(2)

print("Switch initiated")

				
def handle_button():

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
