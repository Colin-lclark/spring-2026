from graphics import *
import random

GRAPH_SIZE = 50
WINDOW_SIZE = [1000, 1000]
SQUARE_TYPES = {'red': 'X','blue': 'O','empty': ' ','disred': '*X','disblue': '*O'}
DEFAULT_INPUT = [0.4, 0.5, 0.3]

def main(input : list):

    [red, blue, segregation] = input #getInput()
    #Stops code if the input(s) is erroneous
    while red + blue > 100 or segregation > 100:
        if red + blue > 100:
            print("ERROR: Red + Blue can't be greater than 100")
        elif segregation > 100:
            print("ERROR: Segregation can only go up to 100")
        [red, blue, segregation] = getInput()
        
    #Set up graph and return shuffled graph
    win = GraphWin("Segregation Graph", WINDOW_SIZE[0], WINDOW_SIZE[1], autoflush=False)
    board = grid(SQUARE_TYPES, red, blue, GRAPH_SIZE)
    sq_size = getSquareSize(GRAPH_SIZE, WINDOW_SIZE)
    graphSegregation(win, board, SQUARE_TYPES, sq_size)

    rounds = 0  

    #Keep moving unsatisfied agents and refreshing the graph until all agents are satisfied
    while 0 == 0:      
        dis_agents = markDissatisfiedAgents(board, SQUARE_TYPES, segregation, GRAPH_SIZE)
        adjustSegregation(dis_agents, board, SQUARE_TYPES)
        graphSegregation(win, board, SQUARE_TYPES, sq_size)
        rounds += 1
        if fullSatsifaction(board, SQUARE_TYPES) == True:
            break
        win.getMouse()
        win.delete("all")

    print("Rounds:", rounds) 

    #Wait for user to click once completed, then close graph
    win.getMouse()
    win.close()

def getInput() -> list[int]:
    #Get inputs for each of the necessary values
    print('%Red | %Blue | %Similar ')
    red = float(input())
    blue = float(input())
    similar = float(input())

    return [red, blue, similar]


def grid(squares : dict, red_perc : float, blue_perc : float, graph_size : int) -> list[list[str]]:

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


def getSquareSize(graph_size : int, window_size : list) -> int:
    if window_size[0] < window_size[1]:
        return int(window_size[0]/graph_size)
    else:
        return int(window_size[1]/graph_size)


def getNeighborhood(board : list[list[str]], coords : tuple, graph_size : int) -> list[list[str]]:

    (x, y) = coords
    neighborhood = []
    for i in range(3):
        neighborhood.append([])
        for j in range(3):
            neighborhood[i].append(None)

    if x == 0:
        x += 1
    
    if y == 0:
        y += 1
    
    if x == graph_size - 1:
        x -= 1
    
    if y == graph_size - 1:
        y -= 1
    
    n = 0
    for row in range(x - 1, x + 2):
        m = 0
        for column in range(y - 1, y + 2):
            neighborhood[n][m] = board[row][column]
            m += 1
        n += 1

    return neighborhood
        

def checkAgentSatisfaction(neighborhood : list[list[str]], squares : dict, segregation_perc : int, graph_size) -> str:

    colors = [0, 0]

    if neighborhood[1][1] != squares.get('empty'):

        for row in range(3):
            for column in range(3):

                if (row, column) != (1, 1):

                    if neighborhood[row][column] == squares.get('red'):
                        colors[0] += 1
                    elif neighborhood[row][column] == squares.get('blue'):
                        colors[1] += 1

        total = colors[0] + colors[1]
        if total == 0:
            return neighborhood[1][1]

        if neighborhood[1][1] == squares.get('red') and (colors[0] / total) < segregation_perc:
            return squares.get('disred')
        elif neighborhood[1][1] == squares.get('blue') and (colors[1] / total) < segregation_perc:
            return squares.get('disblue')

    return neighborhood[1][1]
    

def markDissatisfiedAgents(board : list[list[str]], squares : dict, segregation_perc : int, graph_size : int) -> list[str]:

    open_spots = []

    x = 0
    while x < len(board):
        y = 0
        while y < len(board[x]):
            board[x][y] = checkAgentSatisfaction(getNeighborhood(board, (x, y), graph_size), squares, segregation_perc, graph_size)
            if board[x][y] == (squares.get('empty') or squares.get('disred') or squares.get('disblue')):
                open_spots.append(board[x][y])
            y += 1
        x += 1
    return open_spots
    

def adjustSegregation(dis_agents : list[str], board : list[list[str]], squares : dict) -> list[list[str]]:

    for i in range(len(dis_agents)):
        if dis_agents[i] == squares.get('disred'):
            dis_agents[i] = squares.get('red')
        elif dis_agents[i] == squares.get('disblue'):
            dis_agents[i] = squares.get('blue')

    random.shuffle(dis_agents)

    i = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] in [squares.get('empty'), squares.get('disred'), squares.get('disblue')]:
                if i < len(dis_agents):
                    board[r][c] = dis_agents[i]
                    i += 1
    
    return board


def graphSegregation(win : GraphWin, board : list[list[str]], squares : dict, sq_size : int):
    x = 0
    for row in board:
        y = 0
        for column in row:
            agent = Rectangle(Point(x, y), Point(x+sq_size, y+sq_size))
            if column == squares.get('red'):
                agent.setFill('red')
            elif column == squares.get('blue'):
                agent.setFill('blue')
            else:
                agent.setFill('white')
            agent.draw(win)
            y += sq_size
        x += sq_size
    

def fullSatsifaction(board : list[list[str]], squares : dict) -> bool:

    for row in board:
        for column in row:
            if column in [squares.get('disred'), squares.get('disblue')]:
                return False
    return True


if __name__ == "__main__":
    main(DEFAULT_INPUT)