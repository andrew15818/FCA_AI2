# Lesson 3 Project: N-Queens
## Problem Description
Suppose we are given an nxn chessboard again. The goal is to find a valid placement of
queens such that none of them attack each other. 

The goal of this problem is to have the students understand constraints in 
their code. 

When we have some conditions needed to place our queen, we need to have a way of 
selecitng the valid place on the board.
In theory, this problem can be solved for any square board of size n>3.

Given a straightforward approach, the solution used by the program will always result
in the same solution. What I am thinking is choosing a random element in the last column
(e.g. col 7) and place the first queen there.
