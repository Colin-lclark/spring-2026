from graphics import *
import random

GRAPH_SIZE = 50
WINDOW_SIZE = (500, 500)
SQUARE_TYPES = {1: 'red', 2: 'blu', 3: 'empty', 4: 'disred', 5: 'disblue'}

def grid(squares : dict, red_perc : str, blue_perc : str, graph_size : int) -> list[list[str]]:

    total = graph_size * graph_size

    red_count = int(total * red_perc)
    blue_count = int(total * blue_perc)
    empty_count = total - red_count - blue_count

    cells = []

    for i in range(red_count):
        cells.append(squares.get(1))

    for i in range(blue_count):
        cells.append(squares.get(2))

    for i in range(empty_count):
        cells.append(squares.get(3))

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

def initGraph(empty_perc : int, red_perc : int, blue_perc : int, segregation_perc : int, graph_size : int, window_size : tuple):
    window = GraphWin(window_size(1), window_size(2))
    window.getMouse()
    window.close()

def getNeighborhood(board : list[list[str]], coords : tuple, squares : dict, segregation_perc : int, graph_size : int) -> list[list[str]]:

    #If the square at given coordinate is not at the edge of the board
    if coords(1) != (0 or graph_size - 1) and coords(2) != (0 or graph_size - 1):
        return board[coords(1)-1:coords(1)+2][coords(2)-1:coords(2)+2]
    
    #If the square at given coordinate is at the bottom edge of board but not the corner
    elif coords(1) != (0 or graph_size - 1) and coords(2) != 0:
        return board[coords(1)-1:coords(1) - 1:][coords(2) - 1:]
    
    #If given square is at the top edge but not the corner of board
    elif coords(1) != (0 or graph_size - 1):
        return board[coords(1)-1:coords(1) + 2][:coords(2) + 2]
    
    #If given square is on the right edge (not corner)
    elif coords(1) != 0 and coords(2) != (0 or graph_size - 1):
        return board[coords(1)-1:][coords(2)-1:coords(2)+2]
    
    #If given square is on the left edge (not corner)
    elif coords(2) != (0 or graph_size - 1):
        return board[:coords(1)+2][coords(2)-1:coords(2)+2]
    
    #If square is in corner
    else:
        if coords == [0,0]:
            return board[:coords(1)+2][:coords(2)+2]
        elif coords == [0, graph_size-1]:
            return board[coords(1)-1:][:coords(2)+2]
        elif coords == [graph_size-1, 0]:
            return board[:coords(1)+2][coords(2)-1:]
        else:
            return board[coords(1)-1:][coords(2)-1:]

def isSatisfied(neighborhood : list[list[str]], coords : tuple, squares : dict, segregation_perc : int) -> str:
    return ''

def adjustSegregation(graph : list[list[str]], segregation_perc : int) -> list[list[str]]:
    return []