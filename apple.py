from constants import *
import random
import pygame


class Apple:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def relocate(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))
