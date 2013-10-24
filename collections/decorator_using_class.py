
class EntryExit(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print "Entering %s()" % self.func.__name__
        x = self.func(*args, **kwargs)
        print "Exiting %s()" % self.func.__name__
        return x

@EntryExit
def add(*args):
    sum = 0
    for i in args:
        print '... Adding %d to %d' % (i, sum)
        sum += i
    return sum

if __name__ == "__main__":
    print 'Result is', add(1, 3, 5, 7, 9)