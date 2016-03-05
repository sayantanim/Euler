'''Power digit sum:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?'''


def pow_sum(x,pow):
    mul = str(x ** pow)
    add = 0
    for i in range(0, len(mul)):
        add += int(mul[i])

    return add

print(pow_sum(2,1000))
