import pygame
from time import sleep
# Initialize the player, only need once
pygame.mixer.init()

print("fsdfs")

# Load music and play
pygame.mixer.music.load("./sounds/space-odyssey.mp3")
pygame.mixer.music.play()

# The while loop keeps the code running while music is playing
while pygame.mixer.music.get_busy() == True:
    print("not")
    sleep(5)
    pygame.mixer.music.stop()
    continue



print("hello")