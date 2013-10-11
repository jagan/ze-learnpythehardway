def p1():
    # sum of multiples
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

print p1()