import random
import numpy as np

base = 3                    # Rows and columns of board
elems = base * base         # Total number of elements 
squares = elems * elems
#empties = squares * 1 // 2
empties = 15  # Number of empty boxes

def pattern(r, c):
    return (base*(r%base)+r//base+c)%elems
def shuffle(s):
    return random.sample(s, len(s))

def delete_random(board):
    for p in random.sample(range(squares), empties):
        board[p//elems][p%elems] = 0
    return board

def create_board():
    rbase = range(base)
    rows = [g * base + r for g in shuffle(rbase) for r in shuffle(rbase)]
    cols = [g * base + c for g in shuffle(rbase) for c in shuffle(rbase)]
    nums = shuffle(range(1, base*base+1))
    # produce the randomized board
    board = [ [nums[pattern(r, c)]for c in cols] for r in rows] 
    # numpy arrays provide faster indexing/slicing
    board = np.array(board)
    return board

# Check if all numbers appear only once
# type refers to whether we check row/col or block
def check_all_numbers(arr, type='1d'):
    # TODO: Check if the 3x3 block doesn't repeat 
    count = [0] * (elems + 1) # Keep track of the numbers we've seen
    if type == 'block':
        for row in arr:
            for col in row:
                if (count[col] != 0 
                        or col == 0):
                    return False
                else:
                    count[col] += 1
        return True

    # TODO: check if row/col is valid 
    for i in arr:
        # If a number is repeated
        if (count[i] != 0 
                or i == 0):
            return False
            
        else:
            count[i] += 1
    return True

def find_next_point(board):
    rows, cols = board.shape
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                return (i, j)

    return (-1, -1)
def is_solved(board):
    
    # TODO: Check every row and column
    for i, row in enumerate(board):
        if not check_all_numbers(row):
            return False
        # Get the row and check for repeated numbers
        col = board[:,i]
        if not check_all_numbers(col):
            return False
    
 
    # TODO: Check every subsquare
    for i in range(0, elems, base):
        for j in range(0, elems, base): 
            block = board[i:i+(base),j:j+(base)]
            if not check_all_numbers(block, type='block'):    
                return False
    # If we make it this far we know it's valid board
    return True

# Nicely format the board
def print_board(board):
    rows, cols = board.shape
    print('----------------------------------------------')
    for row in range(rows):
        for col in range(cols):
            if col == 0:
                print('| ', end='')
            print('{:^2d} |'.format(board[row][col]), end=' ')
        print('\n|----|----|----|----|----|----|----|----|----|')

    pass
def is_valid(board, i, j, x):
    pass
def solve_new(board):
    if is_solved(board):
        print("Reached end")
        return True
    i, j = find_next_point(board)
    if (i, j) == (-1, -1):
        return True

    for tmp in range(1, elems+1):
        board[i][j] = tmp
        if solve_new(board):
            return True
        board[i][j] = 0

    return False
# Backtracking search    
def solve(board):
    if is_solved(board):
        print("Reached end")
        return 
    (rows, cols) = board.shape
    # TODO: Find the first unsolved location
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0: 
                for i in range(1, elems+1):
                    # TODO: Skip if num already in same row or col
                    if (i not in board[row] 
                            and i not in board[:,col]):
                        board[row][col] = i
                        solve(board) 
    return 
                    
def main():
    # Debug code for new method
    board = create_board()
    delete_random(board)
    print_board(board)
    print(solve_new(board))
    print_board(board)
    '''
    board = create_board()
    delete_random(board)
    print('====Initial Board====')
    print_board(board)
    print('====Solved Board====')
    solve(board)
    print_board(board) 
    '''
if __name__=='__main__':
    main()
