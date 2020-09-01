import time

def min(n1, n2, n3):
    tmp = n1 if n1 <= n2 else n2
    return tmp if tmp <= n3 else n3

# Lesson 4: Edit Distance
def edit_distance_naive(source, target, source_char, target_char):

    # We can just insert len(target)
    if source_char == 0:
        return target_char

    # If target's length is 0, we could just remove all the
    # letters from source string
    if target_char  == 0:
        return source_char

    # If the characters we're comparing are the same, just 
    # continue recursing
    if source[source_char - 1] == target[target_char - 1]:
        return edit_distance_naive(source, 
                                    target, 
                                    source_char - 1, 
                                    target_char)
    return 1 + min(
                edit_distance_naive(source, target, source_char-1, target_char),
                edit_distance_naive(source, target, source_char, target_char-1),
                edit_distance_naive(source, target, source_char-1, target_char-1)
            )

# Store the temporary results in an array
def edit_distance(source, target):
    sol = [[0 for i in range(len(source)+1)] for j in range(len(target)+1)]

    sol[0][0] = 0

    # If source string is empty, delete source_char characters
    for i in range(1, len(source) + 1):
        sol[0][i] = sol[0][i-1] + 1

    # If source string is empty, also can insert target_char characters
    for j in range(1, len(target) + 1):
        sol[j][0] = sol[j-1][0] + 1

    for i in range(1, len(target)+1):
        for j in range(1, len(source)+1):

            # If the two letters are the same, use the same answer
            if source[j-1] == target[i-1]:
                sol[i][j] = sol[i-1][j-1]

            # Take the operation with minimum cost
            else:
                sol[i][j] = 1 + min(sol[i][j-1],
                                    sol[i-1][j],
                                    sol[i-1][j-1])
    
def main():
    input_strings = input('Enter the two strings separated by space: ').split()
    source = input_strings[0]
    target = input_strings[1]
    #print(edit_distance_naive(source, target, len(source)-1, len(target)-1))


    print(edit_distance(source, target))
    
if __name__=='__main__':
    main()
