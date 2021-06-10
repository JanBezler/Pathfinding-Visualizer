def str_to_int_list(s):
    return [int(x) for x in s]


def print_maze(m):
    for i in m:
        l = []
        for j in i:
            l.append(j.symbol)
        print(*l)


with open("labyrinth.txt") as labyrinth:
    start = str_to_int_list(labyrinth.readline().strip().split(" "))
    end = str_to_int_list(labyrinth.readline().strip().split(" "))
    maze_str = labyrinth.read()


class Board():

    def __init__(self, string_maze: str, start: tuple, end: tuple):
        self.start = start
        self.end = end
        self.maze = self.generate_maze(string_maze)
        self.set_start_end()

    def set_start_end(self):
        self.maze[self.start[1]][self.start[0]].symbol = "s"
        self.maze[self.end[1]][self.end[0]].symbol = "e"

    @staticmethod
    def generate_maze(string_maze: str):
        col = 0
        row = 0
        maze = [[]]

        for char in string_maze:
            if char == "\n":
                maze.append([])
                col += 1
                row = 0
            else:
                maze[col].append(Node((col, row), char))
                row += 1

        return maze


class Node():

    def __init__(self, position: tuple, symbol: str):
        self.position = position
        self.visited = False
        self.symbol = symbol

    def visit(self):
        self.visited = True


maze = Board(maze_str, start, end)

print_maze(maze.maze)
