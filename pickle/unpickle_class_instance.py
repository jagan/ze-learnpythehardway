import cPickle as pik
import traceback, logging, sys

def dump_an_obj(obj, file):
    with open(file, "wb") as f:
        pik.dump(obj, f, 2) # Pickle protocol version 2

def read_the_obj(file):
    with open(file, "rb") as f:
        obj = pik.load(f)
        return obj

if __name__ == "__main__":
    fname = 'class-obj.pyobj'
    traceback.print_stack(file=sys.stdout)
    print '-' * 50

    try:
        lis = read_the_obj(fname)
        print lis
    except AttributeError:
        print 'Error loading the class instances!'
        traceback.print_exc(file=sys.stdout)
        logging.exception('Error loading the class instances')

    print 'Importing the Student class into the module'
    from pickle_class_instance import Student
    lis = read_the_obj(fname)
    print lis
