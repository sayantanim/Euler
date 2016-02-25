'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

def pyt_tri_pro(n):
    for a in range(1,n):
        for b in range(a,n):
            for c in range(b,n):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        pro = a*b*c
                        # print(a,b,c,pro)
    return pro

print(pyt_tri_pro(500))


