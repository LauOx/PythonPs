from parse_script import parse_config, ConfigFormat
import random
from collections import deque
from typing import Optional, Tuple, List, Dict

# ---------------------
# Clase para cada celda
# ---------------------
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = self
        self.walls = {"N": True, "S": True, "E": True, "W": True}

    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()
        return self.parent

    def union(self, other):
        root1 = self.find()
        root2 = other.find()
        if root1 != root2:
            root2.parent = root1

# ---------------------
# Clase Laberinto
# ---------------------
class Maze:
    DIR_DELTA = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    DIR_CHAR = {'N': 'N', 'S': 'S', 'E': 'E', 'W': 'W'}

    def __init__(self, data: ConfigFormat):
        self.width: int = data['width']
        self.height: int = data['height']
        self.entry_xy: tuple[int, int] = data['entry']
        self.exit_xy: tuple[int, int] = data['exit']
        self.perfect: bool = data['perfect']
        self.out_file: str = data['output_file']
        self.seed: Optional[int] = data.get('seed')
        self.grid = [[Cell(x, y) for y in range(self.height)] for x in range(self.width)]

    def _remove_wall(self, c1: Cell, c2: Cell):
        if c2.x == c1.x + 1:
            c1.walls["E"] = False
            c2.walls["W"] = False
        elif c2.x == c1.x - 1:
            c1.walls["W"] = False
            c2.walls["E"] = False
        elif c2.y == c1.y + 1:
            c1.walls["S"] = False
            c2.walls["N"] = False
        elif c2.y == c1.y - 1:
            c1.walls["N"] = False
            c2.walls["S"] = False

    def _generate_maze(self):
        walls = []
        for x in range(self.width):
            for y in range(self.height):
                if x < self.width - 1:
                    walls.append((self.grid[x][y], self.grid[x+1][y]))
                if y < self.height - 1:
                    walls.append((self.grid[x][y], self.grid[x][y+1]))

        if self.seed is not None:
            random.seed(self.seed)
        random.shuffle(walls)

        for c1, c2 in walls:
            if c1.find() != c2.find():
                self._remove_wall(c1, c2)
                c1.union(c2)

    # ---------------------
    # Mostrar laberinto
    # ---------------------
    def print_maze(self):
        print(" " + "_ " * self.width)
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                cell = self.grid[x][y]
                line += "_" if cell.walls["S"] else " "
                line += "|" if cell.walls["E"] else " "
            print(line)

    # ---------------------
    # Resolver laberinto con BFS
    # ---------------------
    def solve(self) -> List[str]:
        queue: deque[Tuple[int, int]] = deque([self.entry_xy])
        came: Dict[Tuple[int,int], Optional[Tuple[Tuple[int,int], str]]] = {self.entry_xy: None}

        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) == self.exit_xy:
                break
            for d, (dx, dy) in self.DIR_DELTA.items():
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < self.width
                    and 0 <= ny < self.height
                    and (nx, ny) not in came
                    and not self.grid[cx][cy].walls[d]):
                    came[(nx, ny)] = ((cx, cy), d)
                    queue.append((nx, ny))

        if self.exit_xy not in came:
            return []

        path: List[str] = []
        pos = self.exit_xy
        while came[pos] is not None:
            info = came[pos]
            path.append(info[1])
            pos = info[0]
        return path[::-1]  # de entrada a salida

# ---------------------
# Uso del laberinto
# ---------------------

data = parse_config("config.txt")
maze = Maze(data)  # semilla fija para reproducibilidad
maze.print_maze()
#solution = maze.solve()
#print("Camino más corto:", solution)