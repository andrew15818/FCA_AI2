# Lesson 1 Project: Find optimal number of moves of knight on a chessboard

## Problem Description

Suppose we are given a h x w sized chessboard, and we are given the starting 
position of a knight on the chessboard. If we are given the location we want
the knight to end up in, we need to find the smallest amount of moves that
will get us from start to end.

We can try out different algorithms to see which one is the best, although 
this might be too much for one lesson.

## General approach 

What are the steps we need to solve the problem? Below are my thougths of 
how the program should flow:
1. Clear the board.
2. Ask the user for starting and ending coordinates.
3. Draw the board with a symbol in the knight's starting position. 
4. Use the algorithm to find the best path.
5. Draw the board after all the nodes have been explored, maybe trace the best path.


## Progress
So far, I have implemented the basic input and output, and figured out the 
syntax for a 2D array in python (a list of lists). Kinda ugly, but at least
we get C-like syntax with our lists.

### TODO:
- Think of an algorithm to use (BFS, DFS, A\*, etc...)
- Implement it
- Think of how to break the project into smaller steps
