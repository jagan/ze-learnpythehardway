def outer(x):
    def inner():
        return x
    x += 1
    return inner

def test_closure():
    x = outer(5)
    y = outer(7)
    assert x() == 6
    assert y() == 8
