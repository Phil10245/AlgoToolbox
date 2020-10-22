# Uses python3

'''Primitive Calculator. Using a dynamic programming approach, the problem to be solved is:
Given a number n and given the  the three operations "add 1", "multiply by 2" and "multiply by 3",
calculate the shortest way to get from 1 to n'''

import doctest
import sys

def optimal_sequence(number):
    '''(int) -> list of int

    precondition: number >= 1

    Takes a number and calculates for n in range(2, number + 1) the minimal number of operations.

    The algorithm performs 4 steps:
    1) check if n is divisible by 3. If so, num_needed_actions stores the sum of operations needed
    to get to n. That is 1 (dividing by 3) + the numbers of actions needed to reach n//3.
    If num_needed_actions is the smaller then min_num_operations[n][0] it becomes the new min.
    2) Step 1 is repeated, but for checking n//2.
    3) min_num_operations[n-1][0] is checked and 1 added. If this is a minimum for n, it is stored
    in min_num_operations[n][0]
    min_num_operations[n][0] is the number of operations needed to get to n.
    min_num_operations[n][1] is the previous n from which you got to n.
    4) The sequence is determined by backtracing the numbers and reversed.

    >>> optimal_sequence(1)
    [1]
    >>> optimal_sequence(3)
    [1, 3]
    >>> optimal_sequence(5)
    [1, 2, 4, 5]
    >>> optimal_sequence(21)
    [1, 2, 6, 7, 21]
    >>> optimal_sequence(96234)
    [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
    '''
    min_num_operations = {1:(0,0)}
    sequence = []
    for n in range(2, number + 1):
        min_num_operations[n] = (999999, )
        if n % 3 == 0:
            num_needed_actions = min_num_operations[n // 3][0] + 1
            if num_needed_actions < min_num_operations[n][0]:
                min_num_operations[n] = (num_needed_actions, n // 3)
        if n % 2 == 0:
            num_needed_actions = min_num_operations[n // 2][0] + 1
            if num_needed_actions < min_num_operations[n][0]:
                min_num_operations[n] = (num_needed_actions, n // 2)
        num_needed_actions = min_num_operations[n - 1][0] + 1
        if num_needed_actions < min_num_operations[n][0]:
            min_num_operations[n] = (num_needed_actions, n - 1)
    retrace_num = number
    while retrace_num > 0:
        sequence.append(retrace_num)
        retrace_num = min_num_operations[retrace_num][1]
    sequence.reverse()
    return sequence

if __name__ == '__main__':
    doctest.testmod()
    n = input("Please enter a number")
    try:
        n = int(n)
    except:
        n = 1
        print("Bad Input.")
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
