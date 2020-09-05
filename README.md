# Project code for the FCA AI2 course

These are the projects for the AI2 course at First Code Academy.
The tentative list for projects include:

## Lesson 1: Optimal moves of a knight on a chessboard
Here, we use different searching algorithms to move a knight across a chessboard.
Given a start and an end position, we can find the optimal move for a knight, and
then mark the nodes along the optimal path.

The main idea is to compare different types of algorithms and when they would be 
better/worse than other ones.

## Lesson 2: Shortest route between ciites 
Calcualting the shortest path to take between two cities is a very important task in modern GPS systems.
In this project we learn about Dijkstra's algorithm for the shortest path in an unweighted graph, which is
one of the most popular algorithms for such a task. 

Since we also learn about graphs in this section, it would be useful to learn how exactly graphs are used in 
Python.

## Lesson 3: 8-Queens
In this lesson we learn about satisfiability and constraint satisfaction, which
will influence our agents when making decisions. 

The 8-queens (we could find a solution for n-queens on an nxn board) problem refers
to finding a valid configuration of 8 queens on a chessboard such that none of them
attack each other.

One such configuration is
![A symmetric solution](img/Nqueens.png) 

where the configuration happens to be symmetrical.

## Lesson 4: Edit Distance
Lesson 4 introduces the idea of greedy algorithms, and we see whether always
taking the best decision at the moment ends up being the best decision in the 
long term (The answer is no). 

We also start touching on the idea of Dynamic Programming and how we could break
down a problem recursively. This approach can be quite intuitive, although 
it can have really high complexity unless we do something about it, like keep 
track of the subproblems we already solved.

For this lesson's project, we are going to do a personal favorite: Edit Distance.
Suppose we have three operations available to us: 
1. Insert a character
2. Delete a character
3. Replace a character

Given two strings, what is the minimum number of operations we have to do to turn one
string into another? 

For example, to turn "horse" into "ros" we would need 3 operations. First, 
we replace "h" with "r". Then, we remove the "r" and "e".
