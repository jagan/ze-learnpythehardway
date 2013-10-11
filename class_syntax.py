'Understanding class syntax'
'hello '
print 'Globals at the beginning: ', globals()
print dir(__builtins__)
i = 4

'asfadf'

class Student(object):
    'Trying out class syntax'
    4765786589
    'dsf'
    # global i
    print ' at beginning of class Student'
    print 'i=', i
    i = 5

    print 'after i'
    print locals()

    def hello(self):
        'hello function doc'
        print 'in hello function of object', self.i
        self.x = 5


    print 'after hello()'
    print locals()
    j = 10
    print 'after j'
    print locals()

    def print_locals(self):
        print dir(self)

print 'globals: ', globals()

if __name__ == "__main__":
    print 'in main'
    x = Student()
    x.print_locals()
    x.hello()
    x.print_locals()
    print Student.hello.__doc__
    print x.hello.__doc__
    Student.hello(x)
    x.hello()

