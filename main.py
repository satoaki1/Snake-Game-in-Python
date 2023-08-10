from constants import *
import pygame
from snake import Snake
from apple import Apple

pygame.init()


def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                if event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                if event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN

        snake.move()

        if snake.body[0] == apple.position:
            snake.grow()
            apple.relocate()

        win.fill(WHITE)
        snake.draw(win)
        apple.draw(win)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
