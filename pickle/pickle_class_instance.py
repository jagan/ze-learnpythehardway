
import cPickle as pik

def dump_an_obj(obj, file):
    with open(file, "wb") as f:
        pik.dump(obj, f, 2) # Pickle protocol version 2

def read_the_obj(file):
    with open(file, "rb") as f:
        obj = pik.load(f)
        return obj

class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return '%s [%s (%s) aged %d]' % (Student.__name__, self.name, self.sex, self.age)

if __name__ == "__main__":
    adam = Student('Adam', 23, 'boy')
    eve = Student('Eve', 20, 'girl')
    print adam
    dump_an_obj([adam, eve], 'class-obj.pyobj')
