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
        # Paredes iniciales: todas presentes
        self.walls = {"N": True, "S": True, "E": True, "W": True}

    # Union-Find con path compression
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
# Función para quitar pared entre dos celdas
# ---------------------
def remove_wall(cell1, cell2):
    if cell2.x == cell1.x + 1:   # cell2 está a la derecha
        cell1.walls["E"] = False
        cell2.walls["W"] = False
    elif cell2.x == cell1.x - 1: # cell2 está a la izquierda
        cell1.walls["W"] = False
        cell2.walls["E"] = False
    elif cell2.y == cell1.y + 1: # cell2 está abajo
        cell1.walls["S"] = False
        cell2.walls["N"] = False
    elif cell2.y == cell1.y - 1: # cell2 está arriba
        cell1.walls["N"] = False
        cell2.walls["S"] = False

# ---------------------
# Crear laberinto 4x4
# ---------------------
def start(Maze) -> None:
    width, height = 5, 5
    grid = [[Cell(x, y) for y in range(height)] for x in range(width)]

    # Crear lista de todas las paredes
    walls = []
    for x in range(width):
        for y in range(height):
            if x < width - 1:
                walls.append((grid[x][y], grid[x+1][y]))  # pared derecha
            if y < height - 1:
                walls.append((grid[x][y], grid[x][y+1]))  # pared abajo

    # Mezclar las paredes aleatoriamente
    random.shuffle(walls)

    # ---------------------
    # Algoritmo de Kruskal
    # ---------------------
    for cell1, cell2 in walls:
        if cell1.find() != cell2.find():
            remove_wall(cell1, cell2)
            cell1.union(cell2)

    # ---------------------
    # Función para mostrar laberinto en consola
    # ---------------------
    def print_maze(grid):
        height = len(grid[0])
        width = len(grid)
        # Imprimir fila superior
        print(" " + "_ " * width)
        for y in range(height):
            line = "|"
            for x in range(width):
                cell = grid[x][y]
                if cell.walls["S"]:
                    line += "_"
                else:
                    line += " "
                if cell.walls["E"]:
                    line += "|"
                else:
                    line += " "
            print(line)

    # Mostrar laberinto generado
    print_maze(grid)