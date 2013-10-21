"Demonstrating type metaclass"
def say_hello(self, who):
    print '%s, %s!' % (self.greeting, who)

Student = type('Student', (object,), {
    'greet': say_hello,
    'greeting': 'Hai'
})

adam = Student()
adam.greet('eve')
