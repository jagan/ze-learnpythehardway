"Named Tuple"
import collections

Student = collections.namedtuple('Student', 'name sex clazz section greet')

def say_hello(self):
    print 'Hello! I am ', self.name

print 'Type of Student', type(Student)

adam = Student('Adam', 'boy', '8', 'B', say_hello)
print adam

eve = Student(clazz='6', sex='girl', section='D', name='Eve', greet=None)
print eve

# accessing by index
for stu in [adam, eve]:
    print "Hai! I am %s. I am a %s student studying in %sth '%s' class!" % stu[:-1]
    print "My properties are:"
    for i, p in enumerate(stu):
        print '%d: %s' % (i, p)

print "Student's properties:"
print dir(Student)
# adam.greet(adam)
