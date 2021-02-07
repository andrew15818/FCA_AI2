from array import *
import queue
import math

# Lesson 1 project
# Change these two values to change the size of the board!
BOARD_HEIGHT = 9
BOARD_WIDTH = 9

# possible x,y movements of a knight
movements = [(-2, 1), 
            (-2, -1),
            (-1, 2),
            (-1, -2),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1)]

# Make a node class to keep track of the parent
class Node: 
    def __init__(self, x, y):
        self.parent = None
        self.child = None
        self.visited = False
        self.x = x
        self.y = y
        self.order = 0 # Print the order in which we explore the nodes

        # For A* algorithm
        self.f = 0 
        self.g = 0
        self.h = 0
    def __gt__(self, node):         
        return (self.f >= node.f)
def is_valid(x, y):
    if x < 0 or y < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT:
        return False
    return True

# Create a new board with correct coordinates 
def new_board():
    board = []
    for i in range(0, BOARD_HEIGHT):
        tmp = []
        for j in range(0, BOARD_WIDTH):
            tmp.append(Node(i, j))
        board.append(tmp)
    return board

# Format the board to look pretty
def print_board(board):
    for i in range(0, BOARD_WIDTH):
        for j in range(0, BOARD_HEIGHT):
            print('{:^2d} |'.format(board[i][j].order), end =' ') 
        print('\n---|----|----|----|----|----|----|----|----|')


# Test if the node is the endpoint
def is_goal(node, e_x, end_y):
    if node.x == e_x and node.y == end_y:
        return True
    return False

# Print the optimal path
def print_path(node):

    if node == None: 
        print('An optimal path is: ')
        return
    print_path(node.parent)
    node.order = node.parent.order + 1 if node.parent != None else 1
    print(f'({node.x}, {node.y})->', end='')


# Breadth First Search
def BFS(board, s_x, s_y, e_x, end_y):
    expanded = 0 
    # TODO: Make our frontier and store the initial tile
    queue = []
    queue.append(board[s_x][s_y])

    # Keep running until the queue is empty or reach end position
    while queue:
        # TODO: Get the oldest node in our queue (closest to the root)
        current = queue.pop(0)
        
        # TODO: Mark the node as visited
        current.visited = True
       
        

        # Check if we reached our destination
        if is_goal(current, e_x, end_y):
            print_path(current)
            return expanded

        # Loop through all the possible moves
        for move in movements:
            # Check the coordinates of the children
            child_x = current.x + move[0]
            child_y = current.y + move[1]
            
            if not is_valid(child_x, child_y):
                continue
            elif board[child_x][child_y].visited == True:
                continue
            
            child = board[child_x][child_y]

            # TODO: Set the current node as the child's parent node
            child.parent = current

            # TODO: append the child to our queue 
            queue.append(child)
        expanded += 1 
       
    return 

# Takes in a board, and starting x,y, and ending x,y respectively
def DFS(board, s_x, s_y, e_x, e_y):
    # Keeping track of the nodes we expanded
    expanded = 0
    # TODO: Create the frontier, where we store the nodes we want to explore
    frontier = []
    # TODO: append the initial node to our stack
    frontier.append(board[s_x][s_y])
    while frontier:
        # TODO: Pop the node we want to explore
        current = frontier.pop()

        # TODO: Mark our node as visited
        current.visited = True
        expanded += 1
        # Check if we are at the goal state
        if is_goal(current, e_x, e_y):
            print_path(current)
            return expanded

        # Loop through all the children
        for move in movements:
            # TODO: get the coordinates of the children's moves
            child_x = current.x + move[0]
            child_y = current.y + move[1]

            # Only loop through valid children
            if not is_valid(child_x, child_y):
                continue
            
            child = board[child_x][child_y]


            if not child.visited:
                # TODO: Set the child node's parent to the current node
                child.parent = current
                # TODO: Append the child node to our frontier 
                frontier.append(child)


                expanded += 1
# "Guess" how much we have left to go
def heuristic(x1, y1, x2, y2):
    # Sum of rows and cols from one point to next
    return (abs(x1 - x2) + abs(y1 - y2))

# Choose the next unvisited node with the lowest heuristic
def heuristic_search(board, s_x, s_y, e_x, e_y):
    # PQueue will order nodes according to hueristic
    frontier = queue.PriorityQueue()
    expanded = 0
    initial = board[s_x][s_y]
    initial.h = heuristic(s_x, s_y, e_x, e_y)
    frontier.put((initial.h, initial))

    while not frontier.empty():
        # Get the node with lowest heuristic
        current = frontier.get()[1]
        if is_goal(current, e_x, e_y):
            print_path(current)
            return expanded
           
        # TODO: Check the possible moves
        for move in movements:
            cx = current.x + move[0]
            cy = current.y + move[1]

            if not is_valid(cx, cy):
                continue

            child = board[cx][cy]

            if child.visited:
                continue
            child.visited = True 
            # TODO: Only explore nodes with a shorter distance
            child.h = heuristic(child.x, child.y, e_x, e_y)
            if child.h < current.h:
                print(f'Adding {child.x},{child.y}')
                child.parent = current 
                frontier.put((child.h, child))
                expanded += 1
    return expanded


# The main function
def main():
    # Print a greeting Message
    while True:
        board = new_board()
        print('------\n'\
            'Enter the name of the algorithm you want to use:\n'\
            '1. BFS\n'\
            '2. DFS\n'\
            '3. Heur\n'\
            '4. quit\n'
            '------'
        )
        algorithm = input('Enter name of algorithm: ').lower()
        if algorithm in ['q','quit']:
            exit()
        # Get the start and end coordinates
        coords = input('Enter the starting coordinates: ').split()
        s_x, s_y = int(coords[0]), int(coords[1])

        coords = input('Enter the ending coordinates: ').split()
        e_x, e_y = int(coords[0]), int(coords[1])
        
        # Execute the indicated algorithm
        if algorithm == 'bfs' or algorithm == '1':
            exp = BFS(board, s_x, s_y, e_x, e_y)
        elif algorithm == 'dfs' or algorithm == '2':
            exp = DFS(board, s_x, s_y, e_x, e_y)
        elif algorithm == 'heur' or algorithm == '3':
            exp = heuristic_search(board, s_x, s_y, e_x, e_y)
        else:
            print('Format incorrect. Try \'bfs/dfs\' and the coordinates separated by a space.')
            continue

        print(f'\nExpanded {exp} nodes using {algorithm}.')     
        print_board(board)
                   
        
    return 0

# execute main function from the start
if __name__=='__main__':
    main()
