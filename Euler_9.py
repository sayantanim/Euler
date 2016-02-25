'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

def pyt_tri_pro(n):
    """

    :param n: Maximum number to search for. In this case, it is 500 because as the problem states,
            there is only one such triplet.
    :return: Product of the Pythogorean triplet whose sum is 1000.
    """
    for a in range(1,n): # a is the smallest number
        for b in range(a,n): # b is the middle number
            for c in range(b,n): # c is the largest number
                if a**2 + b**2 == c**2: # Pythogorus Theorem
                    if a + b + c == 1000:
                        pro = a*b*c
    return pro


def test_Euler_9():
    assert pyt_tri_pro(500) == 31875000


