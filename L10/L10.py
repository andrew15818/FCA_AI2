import random
import numpy as np

base = 3                    # Rows and columns of board
elems = base * base         # Total number of elements 
squares = elems * elems
empties = squares * 3 // 4# Number of empy elements

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
    # Check a 3x3 block
    count = [None] * (elems + 1)
    if type == 'block':
        # Code here
        for row in arr:
            for col in row:
                if count[col] != None:
                    return False
                else:
                    count[col] = 1
        return True
    
    for i in arr:
        # If a number is repeated
        if count[i] != None:
            return False
        else:
            count[i] = 1
    return True


def is_solved(board):
    '''
    # Check every row and column
    for i, row in enumerate(board):
        if not check_all_numbers(row):
            return False
        # Get the row and check for repeated numbers
        col = board[:,i]
        if not check_all_numbers(col):
            return False
    '''
 
    # Check every subsquare
    for i in range(0, elems, base):
        for j in range(0, elems, base): 
            block = board[i:i+(base),j:j+(base)]
            if not check_all_numbers(block, type='block'):
                print(f'Subsquare starting at: {i},{j}')
                return False
    # If we make it this far we know it's valid board
    return True
# TODO: Execute the backtracking
def solve(board):
    if is_solved(board):
        return board 

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                for i in range(elems):
                    board[row][col] = i
                    solve(board)
                    
def main():
    board = create_board()
    for row in board:
        print(row)
    
    delete_random(board)
    is_solved(board)
if __name__=='__main__':
    main()
