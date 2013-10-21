"Static vs Class method"

class Student(object):
    _total = 0

    def __init__(self, name, sex):
        Student._total += 1
        self.name = name
        self.sex = sex

    @classmethod
    def create_student(cls):
        stu = cls('Test', 'M')
        return stu

    @staticmethod
    def total_students_created():
        return Student._total

    def __del__(self):
        print "Student %s getting deleted" % self.name

def print_students_created():
    print 'Total Students created till now:', Student.total_students_created()

if __name__ == "__main__":
    print_students_created()
    adam = Student("Adam", "M")
    eve = Student("Eve", "F")
    print_students_created()
    test = Student.create_student()
    print_students_created()
