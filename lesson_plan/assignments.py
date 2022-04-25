""" MILD assignment: Move n discs from tower source to tower destination and
print the moves of each disc. """

def hanoi_mild(n, source, auxiliary, destination):
    """ Move n discs from tower source to tower destination """
    if n == 0:
        # No more discs to move        
        return None
    
    # move n-1 discs from source to auxiliary
    # you should complete the following line
    # hanoi_mild(n-1, )
    print("Move disc %s from source %s to destination %s" % (n, source, destination))
    
    # move n-1 discs from auxiliary to destination
    # you should complete the following line
    # hanoi_mild(n-1, )

# Call the function like this:
# n = 3 you may try with other number of discs as well 4, 5, 6, ....
# hanoi_mild(n, "A", "B", "C")


""" MEDIUM assignment: Move n discs from tower source to tower destination,
print the moves of each disc and the total number of moves """

def hanoi_medium(n, source, auxiliary, destination):
    """ Move n discs from tower source to tower destination """
    """ Return the total number of moves """
    if n == 0:
        # No more discs to move
        return 0
    
    # move n-1 discs from source to auxiliary
    # you should complete the following line
    # count_b = hanoi_medium(n-1, )
    print("Move disc %s from source %s to destination %s" % (n, source, destination))
    
    # move n-1 discs from auxiliary to destination
    # you should complete the following line
    # count_a = hanoi_medium(n-1, )
    
    # fix the following line, you should return the total number of moves
    return 0

# Call the function like this:
# n = 3 you may try other numbers of discs as well 4, 5,6, ....
# count = hanoi_medium(n, "A", "B", "C")
# print("Total number of moves: %s" % count)
# print("Total number of moves equal to the formula 2**n - 1: %s" % (count == (2**n -1)))


""" SPICY assignment: Move n discs from tower source to tower destination,
print the moves of each disc, the list of disc on each tower after each move
and the total number of moves """

def hanoi_spicy(n, source, auxiliary, destination):
    """ Move n discs from tower source to tower destination """
    """ Return the total number of moves """
    """ List discs on each tower """
    if n == 0:
        # No more discs to move
        return 0
    
    # move n-1 discs from source to auxiliary
    # you should complete the following line
    # count_b = hanoi_spicy(n-1, )
    print("Move disc %s from source %s to destination %s" % (n, source[0], destination[0]))
    
    # move the disc from source list to destination list
    # HINT: source and destination lists should reflect the move of the disc
    # HINT: you should remove the disc from one list and add it to the other one
    # ADD YOUR CODE HERE
    
    # print the lists to see how the discs and towers look like
    print("A: %s, B: %s, C: %s" % (A[1], B[1], C[1]))
    
    # move n-1 discs from auxiliary to destination
    # you should complete the following line
    # count_a = hanoi_spicy(n-1, )
    
    # fix the following line, you should return the total number of moves
    return 0
    
# n = 3 you may try other numbers as well 4, 5,6, ....
# A = ["A", list(range(n,0,-1))]
# B, C = ["B", []], ["C", []]
# print("A: %s, B: %s, C: %s" % (A[1], B[1], C[1]))
# count = hanoi_spicy(n, A, B, C)
# print("Total number of moves: %s" % count)
# print("Total number of moves equal to the formula 2**n - 1: %s" % (count == (2**n -1)))
