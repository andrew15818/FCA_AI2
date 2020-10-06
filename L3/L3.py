# Lesson 3 Project: N-Queens
import random

BOARD_SIZE = 8
Queens = BOARD_SIZE

# Find way to print the board
def print_board(board):

    print('\n---------------------------------------')
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print('{:^2s} |'.format(board[i][j]), end =' ') 
        print('\n---|----|----|----|----|----|----|----|')

# Return a new board
def new_board():
    board = [['*' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

    # Set a queen on random tile in first column to vary the solution
    init_queen = random.randint(0, BOARD_SIZE)
    board[init_queen][0] = 'Q'
    return board

# Check if placing a queen here is feasible
def is_safe(board, row, col):
    '''
    Here, we check:
        1. The tiles on the left-hand side on the same row
        2. The tiles on the upper left diagonal
        3. The tiles on the lower left diagonal
    '''
    # Check the same row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Move along the upper left hand diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Move along the lower left hand diagonal
    for i, j in zip(range(row, BOARD_SIZE, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

# Provide a solution for a board containing col columns
def solve_board(board, col):

    # Return after placing a queen on every column
    if col >= BOARD_SIZE:
        return True

    # Find the spot on the column we can place the queen
    for i in range(0, BOARD_SIZE, 1):
        if is_safe(board, i, col): 
            board[i][col] = 'Q'
            
            # If we can place a queen here and solve the board, return True
            if solve_board(board, col + 1):
                return True
        
        # If we're here, it means we could not solve the board by placing a queen here
        board[i][col] = '*'

    return False

# Main function of our program
def main():
    board = new_board() 
    solve_board(board, 1)
    print_board(board)

if __name__=='__main__':
    main()
