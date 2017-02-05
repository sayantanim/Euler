'''The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
sum.'''


# def diff_sum_sq(num_arr,n):
#     sum_sq = sum(map(lambda i: i**n, num_arr))
#     sq_sum = sum(map(lambda i: i, num_arr)) ** n
#
#     return sq_sum - sum_sq


def diff_sum_pwr(min_num, max_num, pwr):
    """

    :param min_num: Minimum number
    :param max_num: Maximum number
    :param pwr: Number raised to the power
    :return: Difference between power of sum and sum of power
    """
    """ Note: Fails when sum of numbers (not squared) is negative and raised to the power of root.
    Because it becomes a complex number. If round is removed, it gives a value but doesn't mean much."""

    if int(max_num) > 0 and int(min_num) > 0:
        sum_pwr = sum(map(lambda i: i ** pwr, range(int(min_num), int(max_num) + 1)))
        pwr_sum = sum(map(lambda i: i, range(int(min_num), int(max_num) + 1))) ** pwr
        return round(pwr_sum - sum_pwr, 2)
    else:
        sum_pwr = sum(map(lambda i: i ** pwr if i != 0 else False, range(int(min_num), int(max_num) + 1)))
        pwr_sum = sum(map(lambda i: i if i != 0 else False, range(int(min_num), int(max_num) + 1))) ** pwr
        return round(pwr_sum - sum_pwr,4)


def test_euler_6():
    assert diff_sum_pwr(1, 10, 2) == 2640
    assert diff_sum_pwr(5, 100, 3) == 127998561600
    assert diff_sum_pwr(2, 100, 1 / 2) == -599.41
    assert diff_sum_pwr(-100, 10, -3) == 0.0045
