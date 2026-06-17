import keyboard
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("loud_keyboard.mp3")

last_key_time = 0
playing = False

IDLE_TIMEOUT = 0.3  # seconds after last keypress

def on_key(event):
    global last_key_time, playing

    last_key_time = time.time()

    if not playing:
        pygame.mixer.music.play(-1) # loops the audio
        playing = True

keyboard.on_press(on_key)

while True:
    now = time.time()

    if playing and (now - last_key_time) > IDLE_TIMEOUT:
        pygame.mixer.music.stop()
        playing = False

    time.sleep(0.01)