import pygame
import run
import time

board = run.Board("labyrinth.txt")

pygame.init()

screen = pygame.display.set_mode([500, 500])


def draw_maze(maze_, width_, height_, screen_):
    block_size = 0
    origin_position = [0, 0]
    block_size = width_/len(maze_[0])
    origin_position[1] = (height_ - block_size*len(maze_))/2

    color = (0, 0, 0)
    for y, i in enumerate(maze_):
        for x, j in enumerate(i):
            if j.symbol == "#":
                color = (100, 100, 100)
            elif j.symbol == ".":
                if j.visited:
                    color = (180, 250, 20)
                else:
                    color = (250, 250, 30)
            if j.symbol == "s":
                color = (30, 200, 50)
            elif j.symbol == "e":
                color = (220, 40, 20)

            pygame.draw.rect(screen_, color, pygame.Rect(
                x*block_size, y*block_size, block_size, block_size))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for i in board.maze:
        for j in i:
            screen.fill((255, 255, 255))
            j.visit()
            draw_maze(board.maze, 500, 500, screen)
            pygame.display.flip()
            time.sleep(0.2)


pygame.quit()
