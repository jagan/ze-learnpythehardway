"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def p(n):
    x = n * (n + 1) * (2 * n + 1) / 6
    y = n * (n + 1) / 2
    y = y * y
    return y - x

print p(100)