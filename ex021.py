import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while(pygame.event.wait()): pass
#while(pygame.mixer.music.get_busy()): pass