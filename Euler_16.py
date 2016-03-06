'''Power digit sum:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?'''


def pow_sum(num, pow):
    """

    :param num: Number for which power is to be raised
    :param pow: Power
    :return: Sum of the digits after raising the number to its power.
    """
    mul = str(round(num ** pow))
    if mul[0] == '-':  # In case a negative number is raised to an odd power, condition to be satisfied.
        mul = mul[1:]  # Removing the '-' sign.
    add = 0
    for i in range(0, len(mul)):
        add += int(mul[i])
    return mul, add


def test_euler_16():
    assert pow_sum(2, 15) == ('32768', 26)
    assert pow_sum(3.5, 20) == ('76095835016', 50)
    assert pow_sum(5, 20.3) == ('154557857198025', 72)
    assert pow_sum(-5, 20) == ('95367431640625', 61)
    assert pow_sum(-5, 19) == ('19073486328125', 59)
