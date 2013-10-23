
def outer():
    x = 4
    def inner():
        print x
        del x
    inner()

outer()