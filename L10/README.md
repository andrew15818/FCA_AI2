# Project 10: Sudoku Solver
Sudoku is a game where we have a 9x9 board of numbers and we have to organize it
in such a way that each number 1-9 only occurs once in every row, column, and inside
each 3x3 subsquare.

## Approach
Our approach is to use a backtracking method. Each iteration, we have a possible list of numbers
that we could solve the board with at a given position. Then we try and solve a board using the
number in question and backtrack if we find it to not be possible.
