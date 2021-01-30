# Lesson 1 Project: Find optimal number of moves of knight on a chessboard

## Problem Description

Suppose we are given a h x w sized chessboard, and we are given the starting 
position of a knight on the chessboard. If we are given the location we want
the knight to end up in, we need to find the smallest amount of moves that
will get us from start to end.

We can try out different algorithms to see which one is the best, although 
this might be too much for one lesson.

## Running the code
To run the code, from the cli type in
```shell
python L1.py
```
Then type `bfs` or `dfs` to choose the algorithm. The start and end coordinates
should be space-separated, e.g. `1 0`.

## General approach 
I would like to compare/contrast different approaches to searching for a solution
using some of the methods we learned from AC260.

I was thinking of having the students fill out the code for the main algorithms
and choosing one via a message.

What are the steps we need to solve the problem? Below are my thougths of 
how the program should flow:
1. Clear the board.
2. Ask the user for starting and ending coordinates.
3. Draw the board with a symbol in the knight's starting position. 
4. Use the algorithm to find the best path.
5. Draw the board after having the algorithm applied to it. Maybe have the order
in which the nodes are explored.

For the time being, I have three algorithms we are going to test:
1. BFS
2. DFS
3. A\*

### BFS

Breadth-First Search tries to search all the nodes in a level of the search tree
before moving on to the next level.
The major steps in this algorithm go as follows:
1. Create a queue used to keep the nodes we are to explore.
2. Append the initial position to the queue.
3. Pop the oldest node in the list.
4. Check if it is the goal.
5. Loop through all its neighbors, and if there are neighors who have not 
been visited, add them to the end of the queue.

### DFS

Depth-First Search works by always taking the node that was most recently
added and looping through its children. This means that we always follow
a path until we have reached the goal, or all the node's children have been
visited.

The general steps are:
1. create the **frontier** (this separates the already explored nodes from
the completely unexplored nodes.
2. Add the initial node to the frontier.
3. Pop the newest node from the frontier.
4. Loop through this node's children and add them to the frontier if they 
haven't been visited before.


## A\*
The two previous algorithms are examples of **uninformed** search algorithms.
They don't know much about the rest of the board other than the children of the
current node and its related information.

With the A\* algorithm, we use a **heuristic** function, or a function
which estimates how far we have left until our goal node. We use the 
heuristic node to inform our decision on which node to use for our next 
move.
