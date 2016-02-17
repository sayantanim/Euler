# Fibonnaci Series and then sum of even numbers of that series

'''Version 1:'''

# def eve_fib(a, b, k):
#     l = [a, b]
#     sum = 0
#     while b + a < k:
#         a, b = b, b + a
#         l.append(b)
#     for i in l:
#         if i % 2 == 0:
#             sum = sum + i
#
#     return sum

# '''Version 2:'''
#
#
# def eve_fib(a, b, k):
#     l = [a, b]
#     while b + a < k:
#         a, b = b, b + a
#         l.append(b)
#     return sum(filter(lambda i: (i % 2 == 0), l))


'''Version 3:'''


# -*- coding: utf-8 -*-


def eve_fib(num1, num2, max_num, div):
    """

    :param num1: 1st number of the series (non-negative numbers only)
    :param num2: 2nd number of the series (non-negative numbers only)
    :param max_num: Maximum number (non-negative numbers only)
    :param div: The numbers in the series should be multiples of which number?
    :return: sum of numbers in the Fibonacci series which are multiples of div
    """
    fib_lst = [num1, num2]  # First 2 numbers in the series
    while num2 + num1 < max_num:
        num1, num2 = num2, num2 + num1
        # 1st number becomes 2nd number while 2nd number becomes sum of the number itself and the previous number
        fib_lst.append(num2)
    return sum(filter(lambda i: (i % div == 0), fib_lst))


print(eve_fib(2, 5.2, 50000.9, 2))


def test_Euler_2():  # Cannot take -ve numbers. Goes into an infinite loop.
    assert eve_fib(1, 2, 4000000, 3) == 2550408
    assert eve_fib(2, 5, 50000, 5) == 6765
    assert eve_fib(2, 4.2, 50000, 5) == 36775  # Takes in floats
    assert eve_fib(2, 5.2, 50000.9, 2) == 43928  # Takes in floats