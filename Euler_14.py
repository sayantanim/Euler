''' Longest Collatz sequence:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million. '''


def coll(n):
    """

    :param n: Maximum positive integer till which the Collatz Sequence should be found
    :return: Count of the chain in the Collatz Sequence
    """
    cnt = 1  # Minimum length of the chain
    while n > 1:  # n will always be a positive integer
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        cnt += 1
    return cnt


def max_coll(n):
    """

    :param n: Maximum positive integer till which the Collatz Sequence should be found
    :return: Maximum length of the Collatz Sequence and the number itself
    """
    return max((coll(n), n) for n in range(0, n))


def test_euler_14():
    assert max_coll(1000000) == (525, 837799)
    assert max_coll(100000) == (351, 77031)
