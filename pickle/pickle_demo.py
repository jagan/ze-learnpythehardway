
import pickle

FILE_NAME = "dump.pyobj"

def dump_an_obj(obj, file):
    with open(file, "wb") as f:
        pickle.dump(obj, f) # Pickle version 0

def read_the_obj(file):
    with open(file, "rb") as f:
        obj = pickle.load(f)
        return obj

class Student(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return '%s [%s (%s) aged %d]' % (Student.__name__, self.name, self.sex, self.age)

if __name__ == "__main__":
    my_list = range(1000)
    print my_list
    dump_an_obj(my_list, FILE_NAME)
    obj = read_the_obj(FILE_NAME)
    print obj

    adam = Student('Adam', 23, 'boy')
    eve = Student('Eve', 20, 'girl')
    print adam
    dump_an_obj([adam, eve], 'obj2.pyobj')
    obj = read_the_obj('obj2.pyobj')
    print obj

    dump_an_obj(Student, 'StudentClass.pyobj')
    stu_class = read_the_obj('StudentClass.pyobj')
    print stu_class
    mary = stu_class('Mary', 26, 'women')
    print mary