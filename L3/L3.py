# Lesson 3 Project: N-Queens
BOARD_SIZE = 8

# Find way to print the board
def print_board(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print('{:^2d} |'.format(board[i][j].order), end =' ') 
        print('\n---|----|----|----|----|----|----|----|----|')

# Check if placing a queen here is feasible
def is_safe(board, row, col):
    pass

# Here is the main problem 
def solve_board(board):
    pass

# Main function of our program
def main():

if __name__=='__main__':
    main()
