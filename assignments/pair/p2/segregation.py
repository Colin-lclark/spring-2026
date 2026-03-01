from graphics import *
import random

GRAPH_SIZE = 50
WINDOW_SIZE = (500, 500)
SQUARE_TYPES = {'red': 'X','blue': 'O','empty': None,'disred': '*X','disblue': '*O'}

def main():


def graphSegregation(empty_perc : int, red_perc : int, blue_perc : int, segregation_perc : int, graph_size : int, window_size : tuple):
    window = GraphWin(window_size(1), window_size(2))
    window.getMouse()
    window.close()

def grid(squares : dict, red_perc : str, blue_perc : str, graph_size : int) -> list[list[str]]:

    total = graph_size * graph_size

    red_count = int(total * red_perc)
    blue_count = int(total * blue_perc)
    empty_count = total - red_count - blue_count

    cells = []

    for i in range(red_count):
        cells.append(squares.get('red'))

    for i in range(blue_count):
        cells.append(squares.get('blue'))

    for i in range(empty_count):
        cells.append(squares.get('empty'))

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

def getNeighborhood(board : list[list[str]], coords : tuple, squares : dict, segregation_perc : int, graph_size : int) -> list[list[str]]:

    #If the square at given coordinate is not at the edge of the board
    if coords(1) != (0 or graph_size - 1) and coords(2) != (0 or graph_size - 1):
        return [board[coords(1)-1:coords(1)+2][coords(2)-1:coords(2)+2], 'mid'] 
    
    #If the square at given coordinate is at the bottom edge of board but not the corner
    elif coords(1) != (0 or graph_size - 1) and coords(2) != 0:
        return [board[coords(1)-1:coords(1) - 1:][coords(2) - 1:], 'bottom']
    
    #If given square is at the top edge but not the corner of board
    elif coords(1) != (0 or graph_size - 1):
        return [board[coords(1)-1:coords(1) + 2][:coords(2) + 2], 'top']
    
    #If given square is on the right edge (not corner)
    elif coords(1) != 0 and coords(2) != (0 or graph_size - 1):
        return [board[coords(1)-1:][coords(2)-1:coords(2)+2], 'right']
    
    #If given square is on the left edge (not corner)
    elif coords(2) != (0 or graph_size - 1):
        return [board[:coords(1)+2][coords(2)-1:coords(2)+2], 'left']
    
    #If square is in corner
    else:
        if coords == [0,0]:
            return [board[:coords(1)+2][:coords(2)+2], 'topleft']
        elif coords == [0, graph_size-1]:
            return [board[coords(1)-1:][:coords(2)+2], 'topright']
        elif coords == [graph_size-1, 0]:
            return [board[:coords(1)+2][coords(2)-1:], 'botright']
        else:
            return [board[coords(1)-1:][coords(2)-1:], 'botleft']
        

def checkSatisfaction(neighborhood : list[list[list[str]]], squares : dict, segregation_perc : int, graph_size) -> str:

    #Red, Blue
    colors = [0, 0]

    #Location dictionary that specifies what the right row and column values are for the agent in neighborhood
    square_location = {'mid' or 'bottom' or 'botright' or 'right': (1, 1), 'top' or 'topright': (0, 1), 'botleft' or 'left': (1, 0), 'topleft': (0, 0)}
    (x, y) = square_location.get(neighborhood[2])

    #If the agent (square) is not empty
    if neighborhood[0][x][y] != squares.get('empty'):

        for row in range(graph_size):
            for column in range(graph_size):

                #Only counts the color if it is not the specified agent (and not empty)
                if (row, column) != (x, y):

                    #Count number of reds and blus
                    if neighborhood[0][row][column] == squares.get(1):
                        colors[0] += 1
                    elif neighborhood[0][row][column] == squares.get(2):
                        colors[1] += 1

        #Return a dissatisfied value (from dictionary) if the agent is satisfied (if the percent of neighbors in the area is greater than or equal to segregation_perc)
        if neighborhood[0][x][y] == squares.get(1) and (100 * (colors[0] / (colors[0] + colors[1]))) < segregation_perc:
            return squares.get('disred')
        elif neighborhood[0][x][y] == squares.get(2) and (100 * (colors[1] / (colors[0] + colors[1]))) < segregation_perc:
            return squares.get('disblue')

    #Returns same value if empty or satsified
    else:
        return neighborhood[0][x][y]
    

def markDissatisfiedAgents(board : list[list[str]], squares : dict, segregation_perc : int, graph_size : int) -> list[str]:

    open_spots = []

    #Mark dissatisfied agents by adding each empty and dissatisfied value to an empty array
    for row in board:
        for column in row:
            column = checkSatisfaction(getNeighborhood(board, (row, column), squares, segregation_perc, graph_size), squares, segregation_perc)
            if column == (squares.get('empty') or squares.get('disred') or squares.get('disblue')):
                open_spots.append(column)
    return open_spots
    

def adjustSegregation(dis_agents : list[str], board : list[list[str]], squares : dict, segregation_perc : int, graph_size : int) -> list[list[str]]:

    #Set dissatisfied agents back to satisfied for future rounds
    for value in dis_agents:
        if value == squares.get('disred'):
            value = squares.get('red')
        elif value == squares.get('disblue'):
            value = squares.get('blue')

    #Shuffle empty and dissatisfied agents
    random.shuffle(dis_agents)

    #Put shuffled agents in place of unshuffled agents
    i = 0
    for row in board:
        for column in row:
            if column == (squares.get('empty') or squares.get('disred') or squares.get('disblue')):
                column = dis_agents[i]
                i += 1

    #Return modified board
    return board


if __name__ == "__main__":
    main()