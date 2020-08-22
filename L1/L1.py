from array import *
import argparse

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
        self.visited = False
        self.x = x
        self.y = y
        self.order = 0 # Print the order in which we explore the nodes
        
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
    for i in range(0, BOARD_HEIGHT):
        print('----------------------------------------------')
        for j in range(0, BOARD_WIDTH):
            # print the coordinates without a newline
            print(f'| {board[i][j].order} ' , end=' ')
        print("|\n")

# Test if the node is the endpoint
def is_goal(node, end_x, end_y):
    if node.x == end_x and node.y == end_y:
        return True
    return False

# Print the optimal path
def print_path(node):
    tmp = node
    while tmp.parent is not None:
        print(f'<-({tmp.x}, {tmp.y}) ', end=' ')
        tmp.order = tmp.parent.order + 1
        tmp = tmp.parent
    print('\n')
    return

# Breadth First Search
def BFS(board, start_x, start_y, end_x, end_y):
    expanded = 0 
    # Store the nodes in the frontier
    queue = []
    queue.append(board[start_x][start_y])

    # Keep running until the queue is empty or reach end position
    while queue:
        current = queue.pop(0)
        
        current.visited = True
        #print(f'Currently seeing {current.x}, {current.y}')

        # Check if we reached our destination
        if is_goal(current, end_x, end_y):
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
            child.parent = current # Try to record the children instead of the parents
            current.child = child
    
            queue.append(child)
        expanded += 1
    return 

def DFS(board, s_x, s_y, e_x, e_y):
    # Keeping track of the nodes we expanded
    expanded = 0
    # TODO: Create the frontier, where we store the nodes we want to explore
    frontier = []
    # TODO: append the initial node to our stack
    frontier.append(board[s_x][s_y])
    while frontier:
        # TODO: get the node in our array we want to store
        current = frontier.pop()
        current.visited = True

        # Check if we are at the goal state
        if is_goal(current, e_x, e_y):
            print_path(current)
            return expanded

        # Loop through all the children
        for move in movements:
            child_x = current.x + move[0]
            child_y = current.y + move[1]

            # Only loop through valid children
            if not is_valid(child_x, child_y):
                continue
            
            child = board[child_x][child_y]


            if not child.visited:
                child.visited = True
                child.parent = current
                frontier.append(child)
                expanded += 1
         

# TODO: Maybe add more algorithms later, such as A*, ID, DFS, etc...
# The main function
def main():
    # Print a greeting Message
    while True:
        board = new_board()
        print('------\n'\
            'Enter the name of the algorithm you want to use:\n'\
            '1. BFS\n'\
            '2. DFS\n'\
            '3. A_STAR\n'\
            '4. quit\n'
            '------'
        )
        algorithm = input('').lower()
        if algorithm == 'quit':
            exit()
        
        # Get the start and end coordinates
        coords = input('Enter the starting coordinates: ').split()
        start_x, start_y = int(coords[0]), int(coords[1])

        coords = input('Enter the ending coordinates: ').split()
        end_x, end_y = int(coords[0]), int(coords[1])
        
        # Execute the indicated algorithm
        if algorithm == 'bfs':
            exp = BFS(board, start_x, start_y, end_x, end_y)
        elif algorithm == 'dfs':
            exp = DFS(board, start_x, start_y, end_x, end_y)
        elif algorithm == 'a_star':
            print('chose a_star')
        else:
            print('Sorry. I don\'t recognize this one.')
            
        print(f'Expanded {exp} nodes using {algorithm}.')
    return 0

# execute main function from the start
if __name__=='__main__':
    main()
