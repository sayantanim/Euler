'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?'''

from math import factorial

def fact(row,col):
    n = row + col # no. of rows + no. of columns in any direction to reach the end needs these no. of moves.
    move = factorial(n) / (factorial(row)*factorial(n-row)) # n!/r!(n-r)!
    return move

print(fact(20,20))

