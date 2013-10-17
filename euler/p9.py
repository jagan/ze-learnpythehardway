# coding=utf-8
"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Hint: If a2 + b2 = c2, then there exists 2 positive numbers m and n, such that m > n and
a = m2 – n2, b = 2*m*n, c = m2 + n2

Simplification:

a + b + c =  1000
2m^2 + 2mn = 1000
m^2 + mn = 500
m * (m + n) = 500
(x - n) * x = 500
n = (500 - m2) / m

"""

def second_half():
    print 'second half'
    for m in range(250, 500):
        for n in range(250):
            if m * (m + n) == 500:
                yield (m, n)
    return

def first_half():
    print 'first half'
    for m in range(250, -1, -1):
        for n in range(m, 0, -1):
            if m * (m + n) == 500:
                yield (m, n)
    return

def combinations():
    for result in second_half():
        yield result
    for result in first_half():
        yield result

def check_rules(result):
    if not result:
        return False
    print 'checking ', result
    m, n = result
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    if a * a + b * b != c * c:
        return False
    if a + b + c != 1000:
        return False
    print '(m, n)', result
    return (a, b, c)


def p():
    for combi in combinations():
        result = check_rules(combi)
        if result:
            print result
            a, b, c = result
            product = a * b * c
            print 'abc =', product
            print (a*a, b*b, a*a+b*b, c*c)
            return product
    print "Couldn't find solution"
    return None

if __name__ == "__main__":
    p()