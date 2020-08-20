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
        for j in range(0, BOARD_WIDTH):
            # print the coordinates without a newline
            print(f"({board[i][j].x}, {board[i][j].y}) ", end='')
        print("\n")

# Breadth First Search
def search(board, start_x, start_y, end_x, end_y):
    
    # Store the nodes in the frontier
    queue = []
    queue.append(board[start_x][start_y])

    # Keep running until the queue is empty or reach end position
    while queue:
        current = queue.pop(0)
        
        current.visited = True
        print(f'Currently seeing {current.x}, {current.y}')
        # Check if we reached our destination
        if current.x == end_x and current.y == end_y:
            print('\tReached our destination :D')
            return 
        # Add the children of current node to frontier
        for move in movements:
            # Check the coordinates of the children
            child_x = current.x + move[0]
            child_y = current.y + move[1]
            
            if not is_valid(child_x, child_y):
                continue
            elif board[child_x][child_y].visited == True:
                continue
            print(f'\tChecking the children: ({child_x}, {child_y})')
            child = board[child_x][child_y]
            child.parent = current
            child.order = child.parent.order + 1
            queue.append(child)
    return 
# TODO: Maybe add more algorithms later, such as A*, ID, DFS, etc...
# The main function
def main():

    board = new_board()
    # Get the start coordinates as integers
    coords = input("Input starting x y: ")
    start_x, start_y = coords.split()
    start_x, start_y = int(start_x), int(start_y)

    # Get the end coordinates as integers
    coords = input("Input ending x y: ")
    end_x, end_y = coords.split()
    end_x, end_y = int(end_x), int(end_y)
    print(f"Going from ({start_x}, {start_y}) to ({end_x}, {end_y})")

    search(board, start_x, start_y, end_x, end_y)
    return 0

# execute main function from the start
if __name__=='__main__':
    main()
