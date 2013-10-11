def fibonacci(limit):
    a, b = 1, 1
    while b < limit:
        a, b = b, a + b
        print a, ', '
        yield a

def p2():
    # sum of fibonacci
    return sum(i for i in fibonacci(4000000) if i % 2 == 0)

print p2()
