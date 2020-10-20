# Uses python3

'''Algorithm developed for an assignment in course Algorithmic Toolbox on Coursera.

Task is to calculate a minimum of coins needed to change a given amount.
Implemented is a dynamic programming solution'''

import sys

def get_change(money, change):
    '''(int, list of int) -> int

    Calculates how many coins with the values given in change are needed to match amount of money.

    >>>get_change(2, [1])
    2
    >>>get_change(100, [1, 10])
    10
    >>>get_change(39, [1,3,5])
    9
    '''

    coins = change
    min_num_coins = {0: 0}
    for amount in range(1, money + 1):
        min_num_coins[amount] = 999999
        for coin in coins:
            if amount >= coin:
                num_coins_needed = min_num_coins[amount - coin] + 1
                if num_coins_needed < min_num_coins[amount]:
                    min_num_coins[amount] = num_coins_needed
    return min_num_coins[money]


if __name__ == '__main__':
    m = input("Please enter the amount to be changed: ")
    coins = input("\nPlease enter the coins t be used seperated with a space.\nfor example: 3 10 1\n")
    try:
        m = int(m)
    except:
        print("Bad input for amount.")
        m = 10
    try:
        coins = coins.split()
        coins_lst = []
        for c in coins:
            coins_lst.append(int(c))
    except:
        print("Bad input for coins.")
        coins_lst = [2]

    print(f"To change amount {m} you need {get_change(m, coins_lst)} of coins\ngiven the coins {coins_lst}.")

#test
#print("so many coins needed:", get_change(421))
