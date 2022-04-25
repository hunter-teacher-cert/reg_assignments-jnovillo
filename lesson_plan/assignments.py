""" MILD assignment: Move n discs from tower source to tower destination and
print the moves of each disc. """

def hanoi_mild(n, source, auxiliary, destination):
    """ Move n discs from tower source to tower destination. """
    if n == 0:
        # No more discs to move
        return None
    # move n-1 discs from source to auxiliary
    hanoi_mild(n-1, source, destination, auxiliary)
    print "Move disc %s from source %s to destination %s" % (n, source[0], destination[0])
    # move n-1 discs from auxiliary to destination
    hanoi_mild(n-1, auxiliary, source, destination)

# Call the function like this:
# n = 3
# hanoi_mild(n, "A", "B", "C")


""" MEDIUM assignment: Move n discs from tower source to tower destination,
print the moves of each disc and the total number of moves """

def hanoi_medium(n, source, auxiliary, destination):
    """ Move n discs from tower source to tower destination. """
    if n == 0:
        # No more discs to move
        return 0
    # move n-1 discs from source to auxiliary
    count_b = hanoi_medium(n-1, source, destination, auxiliary)
    print "Move disc %s from source %s to destination %s" % (n, source[0], destination[0])
    # move n-1 discs from auxiliary to destination
    count_a = hanoi_medium(n-1, auxiliary, source, destination)
    return count_b + count_a + 1

# Call the function like this:
# n = 3
# count = hanoi_medium(n, "A", "B", "C")
# print "Total number of moves: %s" % count
# print "Total number of moves equal to the formula 2**n - 1: %s" % count == (2**n -1)


""" SPICY assignment: Move n discs from tower source to tower destination,
print the moves of each disc, the list of disc on each tower after each move
and the total number of moves """

def hanoi_spicy(n, source, auxiliary, destination):
    """ Move n discs from tower source to tower destination. """
    if n == 0:
        # No more discs to move
        return 0
    # move n-1 discs from source to auxiliary
    count_b = hanoi_spicy(n-1, source, destination, auxiliary)
    print "Move disc %s from source %s to destination %s" % (n, source[0], destination[0])
    # move disc from source to destination
    destination[1].append(source[1].pop())
    print "A: %s, B: %s, C: %s" % (A[1], B[1], C[1])
    # move n-1 discs from auxiliary to destination
    count_a = hanoi_spicy(n-1, auxiliary, source, destination)
    return count_b + count_a + 1
    
# n = 3
# A = ["A", list(range(n,0,-1))]
# B, C = ["B", []], ["C", []]
# print "A: %s, B: %s, C: %s" % (A[1], B[1], C[1])
# count = hanoi_spicy(n, A, B, C)
# print "Total number of moves: %s" % count
# print "Total number of moves equal to the formula 2**n - 1: %s" % (count == (2**n -1))
