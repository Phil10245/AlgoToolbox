# Uses python3

'''With this dynamic programming algorithm we are goiing to solve the problem of "edit distance".
Meaning, that given string A and string B, we assess how different they are from each other, and
how many steps are neccessary, to transform A into B'''

def edit_distance(s, t):
    '''(str, str) -> int

    Compares two strings by tranforming one into the other and counting the actions needed.

    The possible actions with their value are:
    insertion = +1
    deletion = +1
    mismatch = +1
    match = +0

    3 steps are performed:
    1)  We create the table using a dict. With the size length(string_a)+1 X length(string_b)+1
        The first row is initialized with values from 0 to length(string_a)
        The first column is initialized with values from 0 to length(string_b)
    2)  We loop over string_a in the outer loop, in the inner loop we loop over string_b and check
        each time what is the resulting value for each of the 3 actions. The 4th (a match) is
        only possible if the charakters match.
    3)  We fill the whole table and the value in the bottom right corner tells us what the editing
        distance is.

    >>> edit_distance("a", "a")
    0   # Here we only have one match
    >>> edit_distance("abcd", "abfh")
    2   # Here we have 2matches(a,b) and two mismatch(c,d)
    >>> edit_distance("zettel", "yaethel")
    3   # Here we one insertion and 2 mismatch
    '''
    editing_dist = {}

    # initializing the first row
    for _ in range(-1, len(s)):
        editing_dist[(_, -1)] = _ + 1
    #initializing the first column
    for __ in range(-1, len(t)):
        editing_dist[(-1, __)] = __ + 1

    for j in range(len(s)):
        for i in range(len(t)):
            #1) insertion: D(i, j-1) +1
            distance_ins = editing_dist[(j, i - 1)] + 1
            if j >= 0:
                #2) deletion: D(i-1, j) +1
                distance_del = editing_dist[(j - 1, i)] + 1
                #3) mismatch D(i-1,j-1) +1
                distance_mis = editing_dist[(j - 1, i - 1)] + 1
                #4) match D(i-1, j-1)
                distance_mat = 1999999
                if s[j] == t[i]:
                    distance_mat = editing_dist[(j - 1, i - 1)]
                editing_dist[(j,i)] = min(distance_ins, distance_del, distance_mat, distance_mis)
    return editing_dist[(len(s) - 1, len(t) - 1)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
