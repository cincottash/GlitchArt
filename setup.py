import pygame
pygame.init()

canvasSize = 1000

canvas = pygame.display.set_mode((canvasSize, canvasSize))

background = pygame.image.load("assets/background.jpeg")

canvas.blit(background, (0,0))