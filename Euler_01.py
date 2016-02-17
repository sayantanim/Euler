# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

'''Version 1:'''
# def sum_mult(num_arr):
#
#
#     add = 0
#     for i in num_arr:
#         if i % 3 == 0 or i % 5 == 0:
#             add = add + i
#     return add

'''Version 2:'''

# def sum_mult(num_arr):
#
#     return sum(filter(lambda i: (i % 3 == 0 or i % 5 == 0), num_arr))


# print(sum_mult(range(1,1000,5)))


'''Version 3:'''


# -*- coding: utf-8 -*-


def sum_mult(num_arr, num1, num2):
    """

    :param num_arr: Range of numbers. Either only the max number or range(start, stop[, step])
    :param num1: First multiple
    :param num2: Second multiple
    :return: sum of numbers in the range which are multiples of num1 and num2
    """

    return sum(filter(lambda i: (i % num1 == 0 or i % num2 == 0), num_arr))

print(sum_mult(range(1000),3,5.5))

def test_Euler_1():
    assert sum_mult(range(1000), 3, 5) == 196533
    assert sum_mult(range(-1000, 0, 1), 2, 7) == -285787
    assert sum_mult(range(-1000, 0, 5), 4, 9) == -34185
    assert sum_mult(range(1, 1000, 5), 7, 11) == 21584
