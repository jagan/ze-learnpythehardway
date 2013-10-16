"Iterator that iterates over a given sequence, in reverse"

class Reverse(object):
    'Reverse iterator'
    def __init__(self, seq):
        self.seq = seq
        self.index = len(seq) - 1

    def __iter__(self):
        return self

    def next(self):
        if self.index < 0:
            raise StopIteration()
        self.index -= 1
        return self.seq[self.index + 1]

def main():
    my_list = [i*2+1 for i in range(5)]
    print 'my_list:'
    for i in my_list:
        print i,
    print 'Reversed my_list:'
    for i in Reverse(my_list):
        print i,
    print 'Reversed my_list using while and next:'
    reversed_my_list = Reverse(my_list)
    while True:
        try:
            i = reversed_my_list.next()
        except StopIteration:
            print 'End of list'
            break
        print i,
    reversed_my_list.next()

if __name__ == "__main__":
    main()


