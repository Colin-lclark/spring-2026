from graphics import *
import random

GRAPH_SIZE = 50
WINDOW_SIZE = (500, 500)
RED = "red"
BLUE = "blue"
EMPTY = None

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

def checkSquareSatisfaction(board : list[list[str]], RED : str, BLUE : str, EMPTY : str, segregation_perc : int, graph_size : int) -> int:
    for row in range(graph_size - 2):
        for column in range(graph_size - 2):
            if board[row][column] == RED:
                isSatisfied(board, row, column, RED, segregation_perc)
            elif board[row+1][column+1] == BLUE:
                isSatisfied(board, row, column, BLUE, segregation_perc)

    return 1

def isSatisfied(neighborhood : list[list[str]], row : int, column : int, color : str, segregation_perc : int) -> bool:
    total = 0
    matching = 0
    for row in range(row, row + 2):
        for column in range(column, column + 2):





def adjustSegregation(graph : list[list[str]], segregation_perc : int) -> list[list[str]]:
    return []