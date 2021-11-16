#Faça um programa que abra e reproduza um arquivo MP3
#é importante deixar o arquivo mp3 na mesma pasta do arquivo .py
import pygame
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()