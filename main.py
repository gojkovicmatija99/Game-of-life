import time
import queue
import numpy as np
import pygame
import threading
from arrayqueues.shared_arrays import ArrayQueue
from modules.processPool import processPool
from modules.serial import serial

col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

lock = threading.Lock()
queue = ArrayQueue(100)
lastState = None


def stepsGenerator(steps, n, parts):
    global queue
    global lastState
    lock.acquire()
    newSteps = processPool(steps[len(steps) - 1], n, 20, parts)
    for i in range(1, len(newSteps)):
        queue.put(newSteps[i])
    lastState = newSteps[len(newSteps)-1]
    lock.release()


def update(surface, currState, n, sz):
    for row in range(len(currState)):
        for col in range(len(currState)):
            if currState[row, col] == 1:
                clr = col_alive
            else:
                clr = col_background
            rect = pygame.Rect(col * sz, row * sz, sz - 1, sz - 1)
            pygame.draw.rect(surface, clr, rect)


if __name__ == '__main__':
    n = 50
    iterations = 20
    parts = 2
    cellSize = 20
    startState = (np.random.rand(n ** 2).reshape(n, n) > 0.5).astype(np.int8)
    steps = processPool(startState, n, iterations, parts)
    for i in range(len(steps)):
        queue.put(steps[i])
    lastState = steps[len(steps)-1]
    surface = pygame.display.set_mode((n * cellSize, n * cellSize))
    pygame.display.set_caption("John Conway's Game of Life")

    while not queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # or MOUSEBUTTONDOWN depending on what you want.
                print(event.pos)
            elif event.type == pygame.QUIT:
                quit()

        pygame.display.update()
        surface.fill(col_grid)
        currState = queue.get()
        update(surface, currState, n, cellSize)
        pygame.display.update()
        time.sleep(0.1)
        if not lock.locked():
            thread = threading.Thread(target=stepsGenerator, args=(steps, n, parts))
            thread.start()
