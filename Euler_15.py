'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?'''

'''Version 1: '''

# from math import factorial
#
#
# def fact(row, col):
#     n = row + col  # no. of rows + no. of columns in any direction to reach the end needs these no. of moves.
#     routes = factorial(n) / (factorial(row) * factorial(n - row))  # n!/r!(n-r)!
#     return routes
#
#
# print(fact(20, 20))

'''Version 2:'''


def facto(num):
    """

    :param num: Number for which factorial is to be found
    :return: Factorial of the number

    Note: Factorial is calculated for non-negative integer
    """
    prod = 1
    for i in range(1, num + 1):
        prod *= i
    return prod


def grid(row, col):
    """

    :param row: Number of rows in the grid
    :param col: Number of columns in the grid
    :return: Number of possible routes to reach the bottom right when starting at top left
            and moving only right and down.
    """
    n = row + col  # no. of rows + no. of columns in any direction to reach the end needs these no. of moves.
    routes = facto(n) / (facto(row) * facto(n - row))  # n!/r!(n-r)!
    return round(routes)


def test_euler_15():
    assert grid(5, 5) == 252
    assert grid(20, 20) == 137846528820
    assert grid(12, 15) == 17383860
