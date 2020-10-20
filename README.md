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
