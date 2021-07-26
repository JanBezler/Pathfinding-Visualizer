import time
import pygame


def str_to_int_list(str_):
    return [int(i) for i in str_]


def print_maze(maze_):
    for i in maze_:
        l = []
        for j in i:
            l.append(j.symbol)
        print(*l)


def draw_maze(maze_, width_, height_, screen_):
    block_size = 0
    origin_position = [0, 0]
    # if len(maze_[0]) >= len(maze_) and width_ >= height_:
    block_size = width_/len(maze_[0])
    origin_position[1] = (height_ - block_size*len(maze_))/2

    for y, i in enumerate(maze_):
        for x, j in enumerate(i):
            pygame.draw.rect(
                screen_, (100, 100, 100), pygame.Rect(x, y, block_size, block_size))


def node_in(matrix_: list, position_: tuple, y_: int = 0, x_: int = 0):
    try:
        return matrix_[position_[0]+y_][position_[1]+x_]
    except IndexError:
        return Node((-1, -1), "#")


class Board():

    def __init__(self, file_name_: str):
        self.maze_str, self.start, self.end = self.read_maze_from_file(
            file_name_)
        self.maze = self.generate_maze(self.maze_str)
        self.set_start_end()

    @staticmethod
    def read_maze_from_file(file_name_):
        with open(file_name_) as labyrinth:
            start = str_to_int_list(labyrinth.readline().strip().split(" "))
            end = str_to_int_list(labyrinth.readline().strip().split(" "))
            return labyrinth.read(), start, end

    def set_start_end(self):
        self.maze[self.start[0]][self.start[1]].symbol = "s"
        self.maze[self.end[0]][self.end[1]].symbol = "e"

    @staticmethod
    def generate_maze(string_maze_: str):
        col = 0
        row = 0
        maze = [[]]

        for char in string_maze_:
            if char == "\n":
                maze.append([])
                col += 1
                row = 0
            else:
                maze[col].append(Node((col, row), char))
                row += 1

        return maze


class Node():

    def __init__(self, position_: tuple, symbol_: str):
        self.position = position_
        self.visited = False
        self.symbol = symbol_

    def visit(self):
        self.visited = True


class Pathfinder():
    def __init__(self, maze_: list, start_: tuple):
        self.start = start_
        self.maze = maze_
        self.queue = [node_in(maze_, start_)]
        node_in(maze_, start_).visit()

    def neighbor_check(self, neighbor_: Node):
        if neighbor_.symbol != "#" and neighbor_ not in self.queue and not neighbor_.visited:
            neighbor_.visit()
            if neighbor_.symbol == ".":
                neighbor_.symbol = "*"
            self.queue.append(neighbor_)

    def neighbors_queue(self, node_: Node):
        self.neighbor_check(node_in(self.maze, node_.position, 1, 0))
        self.neighbor_check(node_in(self.maze, node_.position, 0, 1))
        self.neighbor_check(node_in(self.maze, node_.position, -1, 0))
        self.neighbor_check(node_in(self.maze, node_.position, 0, -1))

    def find_path(self):
        focus = self.queue[0]
        not_end = True
        while not_end:
            self.neighbors_queue(focus)
            focus = self.queue.pop(0)
            not_end = focus.symbol != "e"
            if focus.symbol == "*":
                focus.symbol = "@"

        else:
            print(f"found {focus.position}")
