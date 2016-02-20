# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# def palin(min, max):
#     pal = []
#     for i in range(min, max + 1, 1):
#         for j in range(min, max + 1, 1):
#             pro = i * j
#             if str(pro) == str(pro)[::-1]:
#                 pal.append(pro)
#     sort_pal = sorted(pal)
#     return sort_pal[-1]

import itertools


def palin(high_num):  # This method works but since every i is multiplied by every j, it takes time.
    """

    :param high_num: Maximum non-negative number upto which the counter will go for multiplication
    :return: Largest palindrom made from the product of two numbers where the highest number is high_num.
    """
    pal = set()
    for i, j in itertools.product(range(int(high_num) + 1), range(int(high_num) + 1)):
        # First Number is i. Second Number is j. This is same
        # as "for i in range(high_num+1): for j in range(high_num+1): which is a nested loop.
        pro = i * j
        if str(pro) == str(pro)[::-1]:
            # Product = Product in reverse order where each digit of the number is indexed. Hence [::-1]
            pal.add(pro)
    sort_pal = sorted(pal)  # Sorting list
    return sort_pal[-1]  # Gives the last number in the list


print(palin(99.5))


def test_euler_4():
    assert palin(999) == 906609
    assert palin(99.5) == 9009
    assert palin(1098) == 1115111
