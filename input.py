import pygame
import time

pygame.init()
import threading

n = 10
screen = pygame.display.set_mode((100 * n, 100 * n))
clock = pygame.time.Clock()
rect = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # or MOUSEBUTTONDOWN depending on what you want.
            click = pygame.mouse.get_pressed()
            x = event.pos[0]
            y = event.pos[1]
            rect = pygame.Rect((x//n)*n, (y//n)*n, n - 1, n - 1)
            pygame.draw.rect(screen, (0, 255, 0), rect)
            pygame.display.update()
        elif event.type == pygame.QUIT:
            quit()
