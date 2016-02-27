'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''



def prim_fac(num):
    n = 2
    fact = []
    while n < num:
        if num % n == 0:
            fact.append(n)
    return fact

print(prim_fac(10))
