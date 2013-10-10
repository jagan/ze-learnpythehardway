def outer():
    a = 5
    def inner():
        b = 4
        print 'Locals of inner():', locals()
    xyz = inner
    print 'Locals of outer():', locals()
    inner()
    print 'Locals of outer() again:', locals()

if __name__ == "__main__":
    outer()
