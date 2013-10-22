
import cPickle as pik

def dump_an_obj(obj, file):
    with open(file, "wb") as f:
        pik.dump(obj, f, 2) # Pickle protocol version 2

def read_the_obj(file):
    with open(file, "rb") as f:
        obj = pik.load(f)
        return obj

if __name__ == "__main__":
    l = [1, 2, 3]
    l.append(l)

    print l
    print l[3]

    fname = 'recursive.pyobj'
    dump_an_obj(l, fname)

    m = read_the_obj(fname)
    print m
    print m[3]

    ####

    l1 = [1, 2, 3]
    print l1
    l2 = l1
    l2.append(4)
    print l1, l2

    fname = 'tuple.pyobj'
    dump_an_obj((l1, l2), fname)

    m1, m2 = read_the_obj(fname)
    print m1, m2
    m2.append(5)
    print 'm1, m2:', m1, m2
    assert m1 is m2
    print 'l1, l2:', l1, l2
    assert not l1 is m1