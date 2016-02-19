# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# def prim_fac(num):
#     n = 2
#     fact = []
#     while n * n <= num:
#         if num % n == 0:
#             num = num / n
#             fact.append(n)
#         n += 1
#     return num


'''Version 2:'''


def prim_fac(num):
    """

    :param num: Number for which the highest Prime Factor has to be found (non-negative numbers and greater than 2 only)
    :return: Highest Prime Factor for the number
    """
    new_num = round(num, 0)  # Round off the number to the nearest natural number.
    if new_num >= 2:  # 2 is the smallest Prime Number
        n = 2
        while n * n <= new_num:
            if new_num % n == 0:
                new_num = new_num / n
            n += 1
        return new_num
    else:
        return "The smallest Prime Number is 2. Enter a number greater than or equal to 2."


print(prim_fac(13195.3))


def test_euler_3():  # Negative numbers cannot be prime.
    assert prim_fac(600851475143) == 6857
    assert prim_fac(13195) == 29
    assert prim_fac(-4) == "The smallest Prime Number is 2. Enter a number greater than or equal to 2."
    assert prim_fac(13195.0) == 29
    assert prim_fac(13195.8) == 6598
    assert prim_fac(13195.5) == 6598
    assert prim_fac(13195.2) == 29
