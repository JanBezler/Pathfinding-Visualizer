def str_to_int_list(s_):
    return [int(x) for x in s_]


def print_maze(m_):
    for i in m_:
        l = []
        for j in i:
            l.append(j.symbol)
        print(*l)


def content_of(matrix_: list, position_: tuple, y_: int = 0, x_: int = 0):
    try:
        return matrix_[position_[0]+y_][position_[1]+x_]
    except IndexError:
        return Node((-1, -1), "#")


with open("labyrinth.txt") as labyrinth:
    start = str_to_int_list(labyrinth.readline().strip().split(" "))
    end = str_to_int_list(labyrinth.readline().strip().split(" "))
    maze_str = labyrinth.read()


class Board():

    def __init__(self, string_maze_: str, start_: tuple, end_: tuple):
        self.start = start_
        self.end = end_
        self.maze = self.generate_maze(string_maze_)
        self.set_start_end()

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
    def __init__(self, maze_: list):
        self.maze = maze_
        self.queue = []

    def neighbor_check(self, neighbor_: Node):
        if neighbor_.symbol != "#" and neighbor_ not in self.queue:
            self.queue.append(neighbor_)

    def neighbors_queue(self, position_: tuple):
        self.neighbor_check(content_of(self.maze, position_, 1, 0))
        self.neighbor_check(content_of(self.maze, position_, 0, 1))
        self.neighbor_check(content_of(self.maze, position_, -1, 0))
        self.neighbor_check(content_of(self.maze, position_, 0, -1))


maze = Board(maze_str, start, end)

p = Pathfinder(maze.maze)
p.neighbors_queue((5, 3))
print(p.queue)

print_maze(maze.maze)
