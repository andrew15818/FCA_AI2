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

Since we also learn about graphs in this section, it would be useful to learn 
how exactly graphs are used in 
Python.

## Lesson 3: 8-Queens
In this lesson we learn about satisfiability and constraint satisfaction, which
will influence our agents when making decisions. 

The 8-queens (we could find a solution for n-queens on an nxn board) problem refers
to finding a valid configuration of 8 queens on a chessboard such that none of them
attack each other.

One such configuration is

![A solution solution](/img/NQueens.png) 



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

## Lesson 5: Linear Regression

This lesson focused on linear regression, or the process of finding a line that 
best explains a pattern of data. We have many (x, y) points of data and we try and 
find the slope and intercept that best draws a line y = mx + b through the rest of 
the data.

The main process we use to do this is called **gradient descent**. Gradient Descent 
finds the direction in which the slope is changing at our current estimate, and we
adjust our estimate in the direction of the (hopefully) global minimum.

The next time we run the algorithm, our guess should give us a lower **error**, or
it should match the data more closely.

In this project, we have a group of data points that (roughly) follow a 
pattern y = mx + b. We try to find this line by finding the appropriate slope and
intercept to use.

The end result should look something like 

![Final Regression](/img/Regression.png)

The line is what we calculate for the training set, and we generalize it to an unseen 
testing set, which is what this image shows.

## Lesson 6: Training a game-playing agent

Lesson 6 introduced supervised and reinforcement learning. The regression done in
Lesson 5 is an example of supervised learning since during training we have access 
to the labels of the training data. This might not be feasible in every scenario,
since sometimes we might have to wait until we see the result of an action.

In this project, we use [openai](https://gym.openai.com)'s gym library. This library
provides many environments to test reinforcement learning. Gym is a great resource
to learn more about algorithms and apply them to games.

