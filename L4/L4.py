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
def edit_distance(source, target, source_char, target_char):
   sol = [[0] * len(source)] * len(target) 

   print(sol)

def main():
    input_strings = input('Enter the two strings separated by space: ').split()
    source = input_strings[0]
    target = input_strings[1]
    #print(edit_distance_naive(source, target, len(source)-1, len(target)-1))
    print(edit_distance(source, target, len(source)-1, len(target)-1))
    
if __name__=='__main__':
    main()
