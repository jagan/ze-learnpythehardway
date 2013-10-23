import cPickle as pik

def dump_an_obj(obj, file):
    with open(file, "wb") as f:
        pik.dump(obj, f, 2) # Pickle protocol version 2

def read_the_obj(file):
    with open(file, "rb") as f:
        obj = pik.load(f)
        return obj

class Foo(object):
    def __init__(self, name, filename):
        self.name = name
        self.log_file = open(filename, 'w')

    def change_name(self, name):
        self.log_file.write('Changing name from %s to %s\n' % (self.name, name))
        self.name = name

    def do_something(self, activity):
        self.log_file.write('Doing activity: %s\n' % activity)

    def __getstate__(self):
        return (self.name, self.log_file.name, self.log_file.tell())

    def __setstate__(self, data):
        self.name, filename, file_position = data
        f = open(filename, 'r+')
        print 'current position: ', f.tell()
        print 'seeking position: ', file_position
        f.seek(file_position)
        self.log_file = f

    def __del__(self):
        self.log_file.close()

if __name__ == "__main__":
    foo1 = Foo('Adam', 'foo.log')
    foo1.change_name('John')
    foo1.do_something('Eating')
    foo1.do_something('Working')
    foo1.do_something('Sleeping')

    fname = 'foo.pyobj'
    dump_an_obj(foo1, fname)

    del foo1

    foo1 = read_the_obj(fname)
    print foo1.name
    foo1.do_something('Playing')
