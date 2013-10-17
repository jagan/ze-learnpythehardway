# coding=utf-8
"""
Largest product in a grid
Problem 11
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

def read_grid(filename, maxx, maxy):
    try:
        file = open(filename)
    except IOError:
        return None
    number_grid = []
    for line in file:
        if not line:
            continue
        numbers_str = line.split(' ')
        if len(numbers_str) != maxy:
            print 'Expected %d numbers in a row. Found %d' % (maxx, len(numbers_str))
            return None
        numbers = []
        for n in numbers_str:
            try:
                num = int(n)
            except ValueError:
                print 'Invalid number in file: ', n
                return None
            numbers.append(num)
        number_grid.append(numbers)
    if len(number_grid) != maxy:
        print 'Expected %d rows of numbers. Found %d' % (maxy, len(number_grid))
        return None
    return number_grid

def print_grid(grid):
    for line in grid:
        print '[',
        for num in line:
            print "%2d" % num,
        print ']'

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.send(None)
        return cr
    return start

@coroutine
def check_biggest():
    biggest = None
    while True:
        a, b, c, d = yield biggest
        product = a * b * c * d
        if (not biggest) or (biggest[4] < product):
            biggest = a, b, c, d, product

def indexes_left_to_right(x, y, num):
    for i in range(x):
        for j in range(y - num + 1):
            yield [(i, j + b) for b in range(num)]

def indexes_up_to_down(x, y, num):
    for i in range(x - num + 1):
        for j in range(y):
            yield [(i + b, j) for b in range(num)]

def indexes_diagonally_up_to_down(x, y, num):
    for i in range(x - num + 1):
        for j in range(y - num + 1):
            yield [(i+b, j+b) for b in range(num)]

def indexes_diagonally_down_to_up(x, y, num):
    for i in range(num - 1, x):
        for j in range(y - num + 1):
            yield [(i-b, j+b) for b in range(num)]

def all_indexes(x, y, num):
    funcs = [indexes_left_to_right, indexes_up_to_down, indexes_diagonally_up_to_down, indexes_diagonally_down_to_up]
    for func in funcs:
        for indexes in func(x, y, num):
            yield indexes

def find_biggest(grid, x, y, num):
    biggest = None
    biggest_checker = check_biggest()
    for indexes in all_indexes(x, y, num):
        prev_biggest = biggest
        print '.. checking index ', indexes
        numbers = (grid[a[0]][a[1]] for a in indexes)
        biggest = biggest_checker.send(numbers)
        if prev_biggest != biggest:
            print 'New biggest found: %s (at %s)' % (biggest, indexes)
    return [indexes, biggest]

def p():
    x, y, num = 20, 20, 4
    grid = read_grid('p11.txt', x, y)
    print_grid(grid)
    biggest = find_biggest(grid, x, y, num)
    print biggest

if __name__ == "__main__":
    print list(indexes_left_to_right(20, 20, 4))
    print list(indexes_up_to_down(20, 20, 4))
    print list(indexes_diagonally_up_to_down(20, 20, 4))
    print list(indexes_diagonally_down_to_up(20, 20, 4))
    p()
