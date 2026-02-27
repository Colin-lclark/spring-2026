from graphics import *
import random

GRAPH_SIZE = 50
WINDOW_SIZE = (500, 500)
RED = "red"
BLUE = "blue"
EMPTY = "empty"

def grid(RED : str, BLUE : str, EMPTY : str, red_perc : str, blue_perc : str, graph_size : int) -> list[list[str]]:

    total = graph_size * graph_size

    red_count = int(total * red_perc)
    blue_count = int(total * blue_perc)
    empty_count = total - red_count - blue_count

    cells = []

    for i in range(red_count):
        cells.append(RED)

    for i in range(blue_count):
        cells.append(BLUE)

    for i in range(empty_count):
        cells.append(EMPTY)

    random.shuffle(cells)

    board = []
    index = 0

    for r in range(graph_size):
        row = []
        for c in range(graph_size):
            row.append(cells[index])
            index += 1
        board.append(row)

    return board

def segregateSquares(empty_perc : int, red_perc : int, blue_perc : int, segregation_perc : int, graph_size : int, window_size : tuple):
    return []

def checkGraphSegregation(graph_array : list[list[str]], red_def : str, blue_def : str, empty_def : str) -> int:
    return 1

def adjustSegregation(graph : list[list[str]], segregation_perc : int) -> list[list[str]]:
    return []