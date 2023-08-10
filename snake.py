from constants import *
import pygame


class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        new_head = ((head_x + new_dir_x) % (WIDTH // CELL_SIZE),
                    (head_y + new_dir_y) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        new_head = ((head_x + new_dir_x) % (WIDTH // CELL_SIZE),
                    (head_y + new_dir_y) % (HEIGHT // CELL_SIZE))
        self.body = [new_head] + self.body

    def draw(self, win):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
