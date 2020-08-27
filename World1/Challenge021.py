
import pygame 

mixer.init()
mixer.music.load('ex01.mp3')
mixer.music.play()
while mixer.music.get_busy() == True: continue
