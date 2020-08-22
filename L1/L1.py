from array import *

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
    while tmpparent is not None:
        print(f'<-({tmp.x}, {tmp.y}) ', end=' ')
        tmp.order = tmp.parent.order + 1
        tmp = tmp.parent
    print('\n')
    return

# TODO: Maybe add more algorithms later, such as A*, ID, DFS, etc...
# The main function
def main():
    # TODO: Create a new board
    board = new_board()

    coords = input("Input starting x y: ")
    start_x, start_y = coords.split()
    start_x, start_y = int(start_x), int(start_y)

    # Get the end coordinates as integers
    coords = input("Input ending x y: ")
    end_x, end_y = coords.split()
    end_x, end_y = int(end_x), int(end_y)
    print(f"Going from ({start_x}, {start_y}) to ({end_x}, {end_y})")
    # TODO: call the search function
    search(board, start_x, start_y, end_x, end_y)

    # TODO: Print the board with some node information 
    print_board(board)
    return 0

# execute main function from the start
if __name__=='__main__':
    main()
