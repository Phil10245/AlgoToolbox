# AlgoToolbox
Going to upload here the algorithms designed in the course Algorithmic Toolbox
## arithmetic.py is my solution to this task:
### Maximum Value of an Arithmetic Expression
#### Problem Introduction
In this problem, your goal is to add parentheses to a given arithmetic expression to maximize its value. max(5 − 8 + 7 × 4 − 8 + 9) =?
#### Problem Description
Task.  
Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
operations using additional parentheses.  
Input Format.  
The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols 𝑠0, 𝑠1, . . . , 𝑠2𝑛.  
Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while each symbol at an odd position is one of three operations from {+,-,*}.  
Constraints.  
0 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).  
Output Format.   
Output the maximum possible value of the given arithmetic expression among different
orders of applying arithmetic operations.  
- Sample 1.  
Input: '1+5'  
Output: '6'  
- Sample 2.  
Input: '5-8+7*4-8+9'  
Output: '200'  
200 = (5 − ((8 + 7) × (4 − (8 + 9))))

## change_dp.py is my solution to this problem:
### Money Change Again
#### Problem Introduction
As we already know, a natural greedy strategy for the change problem does not work correctly for any set of
denominations.   
For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change
6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3).  
Your goal now is to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.
#### Problem Description
Input Format.  
Integer money.  
Output Format.  
The minimum number of coins with denominations 1, 3, 4 that changes money.  
(**Here the uploaded version differs and takes user input as denominations list**)  
Constraints.  
1 ≤ money ≤ 103.
- Sample 1.  
Input: 2  
Output: 2  
- Sample 2.  
Input: 34  
Output: 9  
34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.

## knapsack.py is my solution to this problem:
### Maximum Amount of Gold
#### Problem Introduction
You are given a set of bars of gold and your goal is to take as much gold as possible into
your bag. There is just one copy of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar).
#### Problem Description
Task.  
Given n gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.  
Input Format.  
The first line of the input contains the capacity 𝑊 of a knapsack and the number.  
The next line contains 𝑛 integers 𝑤0, 𝑤1, . . . , 𝑤𝑛−1 defining the weights of the bars of gold.  
Constraints.  
1 ≤ 𝑊 ≤ 10; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . , 𝑤𝑛−1 ≤ 105.  
Output Format.  
Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.  
- Sample 1.  
Input: 10, 1 4 8  
Output: 9  
Here, the sum of the weights of the first and the last bar is equal to 9.

## primitive_calculator.py is my solution to this problem:
### Primitive Calculator
#### Problem Introduction
You are given a primitive calculator that can perform the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥.  
Your goal is given a positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.  
#### Problem Description
Task.  
Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.  
Input Format.  
The input consists of a single integer 1 ≤ 𝑛 ≤ 106.  
Output Format.  
In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1.  
In the second line output a sequence of intermediate numbers. That is, the second line should contain positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎𝑖+1 is equal to either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. If there are many such sequences, output any one of them.  
- Sample 1.  
Input: 1  
Output:  
0  
1
- Sample 2.  
Input: 5  
Output:  
3  
1 2 4 5  
Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3
and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.
- Sample 3.  
Input: 96234  
Output:  
14  
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234  
Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117
96234”.
