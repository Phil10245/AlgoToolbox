'''part of an assignment of the course Algorithmic Toolbox on Coursera.

The function get_maximum_value() implements a dynamic programming approach to solve the task of
calculating the maximal possible value of an expression like "5+3*6-8+7-2*3" when the order of
operations can be freely chosen (setting brackets freely): "(((5+3)*6-8)+7)-2*3".
See the docstring of the function for more examples!'''
# Uses python3

def get_maximum_value(dataset):
    '''(string) -> int

    Takes an arithmetic expression string and returns the maximum possible value, attainable by
    changing the order of operations.

    precondition: string has a number(0-9) on every odd place, every even place has an arithmetic
    symbol(+,-,*).
    Maximal len(string) == 29.


    >>>"2+2*2"
    8
    >>>"5+1-3*10"
    30
    >>>"5-8+7*4-8+9"
    200
    '''
    operations = ""
    no_operation = ""
    for item in dataset:
        if item.isdigit():
            no_operation += item
        else:
            operations += item

    n = len(no_operation)
    # initiating the tables, that store min and max
    minimum = [[9999 for i in range(n)] for i in range(n)]
    maximum = [[-9999 for i in range(n)] for i in range(n)]

    for i in range(n):
        minimum[i][i] = int(no_operation[i])
        maximum[i][i] = int(no_operation[i])
    for s in range(1, n):
        for i in range(0,n-s):
            j = i + s
            minimum[i][j], maximum[i][j] = min_max(i, j, minimum, maximum, operations)
    return maximum[0][-1]


def min_max(i, j, max_mat, min_mat, op_list):
    ''' Calculate the min and max of sub1 and sub2'''

    lowest = []
    highest = []

    for k in range(i,j):
        res_a = evalt(int(max_mat[i][k]), int(max_mat[k+1][j]), op_list[k])
        res_b = evalt(int(max_mat[i][k]), int(min_mat[k+1][j]), op_list[k])
        res_c = evalt(int(min_mat[i][k]), int(min_mat[k+1][j]), op_list[k])
        res_d = evalt(int(min_mat[i][k]), int(max_mat[k+1][j]), op_list[k])
        lowest.append(min(res_a, res_b, res_c, res_d))
        highest.append(max(res_a, res_b, res_c, res_d))

    return min(lowest), max(highest)


def evalt(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    assert False



if __name__ == "__main__":
    print(get_maximum_value(input()))
