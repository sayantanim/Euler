'''The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this
product?'''

'''Mathematical method: Say n = 4. Product 1 = 7*3*1*6; Product 2 = 3*1*6*7; and so on.... Thus the last time this 
multiplication will be performed is when there are just 4 digits left at the end. '''


# def pro(dig, n):
#     gre_pro = 0  # Minimum product is zero for natural numbers. Hence starting with 0
#     for i in range(0, len(dig) - n):  # Assume each digit as a single entity and hence each has an index. And the
#         # maximum range can be the length of the given number minus the number of adjacent digits to be multiplied.
#         # Thus i is the index of each digit.
#         prod = 1  # if this is 0, product will always remain to be '0'
#         for j in range(i,i + n):  # Calculation for product of n adjacent numbers is "731671.." followed by "361717..."
#             # followed by "617176..." and so on. Hence the range starts from index i and ends at index i+n.
#             prod *= int(dig[j:j + 1])  # The multiplication starts with the 1st number, i.e., current index j and
#             # the next index j+1 and continues till it reaches i+13
#         if prod > gre_pro:  # Check f=if current product is greater than the previous product
#             gre_pro = prod  # If current product is greater, then replace greater product with current product
#     return gre_pro


def pro(num, n):
    gre_pro = 0  # Minimum product is zero for natural numbers. Hence starting with 0
    if n >= 0 and len(num) >= n:
        for i in range(0, len(num) - n):  # Assume each digit as a single entity and hence each has an index. And the
            # maximum range can be the length of the given number minus the number of adjacent digits to be multiplied.
            # Thus i is the index of each digit.
            prod = 1  # if this is 0, product will always remain to be '0'
            for j in range(i,
                           i + n):  # Calculation for product of n adjacent numbers is "731671.." followed by
                # "361717..."
                # followed by "617176..." and so on. Hence the range starts from index i and ends at index i+n.
                prod *= int(num[j:j + 1])  # The multiplication starts with the 1st number, i.e., current index j and
                # the next index j+1 and continues till it reaches i+n
            if prod > gre_pro:  # Check if current product is greater than the previous product
                gre_pro = prod  # If current product is greater, then replace greater product with current product
        return gre_pro
    else:
        return 'Length of number should be greater than n. n must always be a natural number.'


print(pro("731671765313306249192251196744265", 5))


def test_euler_8():
    assert pro("731671765313306249192251196744265", 5) == 6048
    assert pro("731671765313306249192251196744265",
               -5) == "Length of number should be greater than n. n must always be a natural number."
    assert pro("7316", 5) == "Length of number should be greater than n. n must always be a natural number."