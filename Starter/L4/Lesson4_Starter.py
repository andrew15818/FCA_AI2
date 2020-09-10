import time

def min(n1, n2, n3):
    tmp = n1 if n1 <= n2 else n2
    return tmp if tmp <= n3 else n3

def edit_distance_naive(source, target, source_char, target_char):

    # We can just insert len(target)
    if source_char == 0:


    # If target's length is 0, we could just remove all the
    # letters from source string
    if target_char  == 0:
       

    # If the characters we're comparing are the same, just 
    # continue recursing
    if source[source_char - 1] == target[target_char - 1]:
     
    # return 1 + the minimum of each operation
    return 

# Store the temporary results in an array
def edit_distance(source, target):
    # Matrix to store our solution


    # If source string is empty, delete source_char characters
    for i in range(1, len(source) + 1):


    # If source string is empty, also can insert target_char characters
    for j in range(1, len(target) + 1):


    for i in range(1, len(target)+1):
        for j in range(1, len(source)+1):

            # If the two letters are the same, use the same answer
            if source[j-1] == target[i-1]:


            # Take the operation with minimum cost
            else:
    # return the appropriate array position      
    return 

def edit(method, source, target):
    if method == 'naive':
        return edit_distance_naive(source, target, len(source), len(target)) 
    elif method == 'dynamic':
        return edit_distance(source, target) 

def main():
    while True:
        method = input('\nNaive or dynamic solution: ').lower()
        if method == 'quit':
            break
        input_strings = input('Enter two strings separated by a space: ').split()
        source = input_strings[0]
        target = input_strings[1]
        sol = edit(method, source, target)  
        print(f'Going from {source} to {target} takes {sol} edits.')



    
if __name__=='__main__':
    main()
