
# Breadth First Search
def solve(board, start_x, start_y, end_x, end_y):
    
    # Store the nodes in the frontier
    queue = []
    queue.append(board[start_x][start_y])

    # Keep running until the queue is empty or reach end position
    while queue:
        current = queue.pop(0)
        
        current.visited = True
        #print(f'Currently seeing {current.x}, {current.y}')

        # Check if we reached our destination
        if is_goal(current, end_x, end_y):
            print_path(current)
            return 

        # Loop through all the possible moves
        for move in movements:
            # Check the coordinates of the children
            child_x = current.x + move[0]
            child_y = current.y + move[1]
            
            if not is_valid(child_x, child_y):
                continue
            elif board[child_x][child_y].visited == True:
                continue
            
            child = board[child_x][child_y]
            child.parent = current # Try to record the children instead of the parents
            current.child = child

            queue.append(child)
    return 

