"""
Large sum
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
def read_numbers(filename, length, count):
    try:
        file = open(filename)
    except IOError:
        return None
    numbers = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        if len(line) != length:
            print 'Expected %d digits in a row. Found %d' % (length, len(line))
            return None
        numbers.append(line)
    if len(numbers) != count:
        print 'Expected %d numbers. Found %d' % (count, len(numbers))
        return None
    return numbers

def print_numbers(numbers):
    for num in numbers:
        print "%s" % num

def add(numbers, carry_on, startI, endI):
    total = carry_on
    for num_str in numbers:
        num = long(num_str[startI:endI])
        print (num_str, num, startI, endI)
        total += num
    print 'total =', total
    total_str = str(total)
    x = (total, long(total_str[0:-10]))
    print x
    return x

def main():
    length = 50
    each_time = 10
    endI = length
    startI = endI - each_time
    numbers = read_numbers('p13.txt', 50, 100)
    total = carry_on = 0
    while endI > 0:
        total, carry_on = add(numbers, carry_on, startI, endI)
        endI -= each_time
        startI = endI - each_time
        if startI < 0: startI = 0
    print total
    print 'Answer:', str(total)[0:10]

if __name__ == "__main__":
    main()
