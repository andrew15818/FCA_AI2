# Lesson 4: Edit Distance

The main problem description is stated in the main README.

Given two strings and three possible operaitons, how could we 
turn one string into anoter using the minimum amount of operations?

## Naive approach

The straightforward approach to edit distance involves recursing
three times at every level, and selecting the cost with minimum action.
e.g.

	return 1 + min(edit_distance(...), 	# cost of inserting
					edit_distance(...),	# cost of replacing 
					edit_distance(...))	# cost of deleting

This approach would have complexity `O(3^n)`, since we recurse three times for every 
time we call this function, or `n` times. 

Instead of having the 3 recursive calls at every time, we could have only a couple
lookups in a 2D array. The recursive part of our function would then become something
like:

	return 1 + min(arr[i-1][j],
					arr[i][j-1]
					arr[i-1][j-1])

which would result in a time complexity of O(n^2) instead.

Maybe we could compare the two approaches to see how fast they are?
