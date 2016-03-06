'''Factorial digit sum:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!'''

'''Version 1:'''

# from math import factorial
#
# def fact_sum(n):
#     fact = str(factorial(n))
#     add = 0
#     for i in range(0, len(fact)):
#        add += int(fact[i])
#     return add
#
# print(fact_sum(100))

'''Version 2:'''


def facto(num):  # Same as in Euler_15.py
    """

    :param num: Number for which factorial is to be found
    :return: Factorial of the number

    Note: Factorial is calculated for non-negative integer
    """
    prod = 1
    for i in range(1, num + 1):
        prod *= i
    return prod


def fact_sum(num):
    """

    :param num: Number for which factorial sum is to be found
    :return: Sum of digits of factorial value
    """
    fact = str(facto(num))
    add = 0
    for i in range(0, len(fact)):
        add += int(fact[i])
    return add


def test_euler_20():
    assert fact_sum(100) == 648
