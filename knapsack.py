'''
Implementation of a non-repetiv, non-fractional knapsack algorithm

Given a set of goldbarren with specific weights the algorithm picks the maximum
number of goldbarren, that fit into a knapsack with given capacity
'''# Uses python3
import sys

def optimal_weight(W, w):
    '''(int, list of ints) -> int

    Calculates maximal value for a given capacity W and list of items w.

    Each item in w can only be taken once. And only completely or not at all.
    The variable value_place stores besides the value also which items were used.
    >>>optimal_weight(5, [1,1,1])
    3
    >>>optimal_weight(1, [2])
    0
    >>>optimal_weight(5, [1,3,4])
    5
    '''
    value = 0
    used_barren = (0,)
    value_place = [[used_barren, value]]
    for i in range(1, W + 1):
        for barren in w:
            if barren <= i:
                if value < barren + value_place[i - barren][1]:
                    if are_barren_available(barren, w, value_place[i - barren][0]):
                        value = barren + value_place[i-barren][1]
                        used_barren = (*value_place[i - barren][0], barren)
        value_place.append([used_barren, value])
    return value_place[-1][1]

def are_barren_available(bar_testing, all, used):
    '''(int, list of ints, list of ints) -> boolean

    Checks if bar_testing is available.

    takes list all and compares it with list used. removing the item from used to
    not count it double. If an item is not in used it's appended to avai_bars.
    Then it checks if the bar_testing is in this list.
    Returns True if bar_testing is in avai_bars. Otherzise False.
    '''

    avai_bars = []
    used = list(used)
    for bar in all:
        if bar in used:
            used.remove(bar)
        else:
            avai_bars.append(bar)
    if bar_testing in avai_bars:
        return True
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
