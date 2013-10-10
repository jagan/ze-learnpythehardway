def func(x):
    return x + 1

def test_func():
    assert func(3) == 4

def add(x, y):
    return x + y

class TestAddition:
    def test_add_zeros(self):
        assert add(0, 0) == 0

    def test_add_zero_with_anything(self):
        assert add(0, 1) == 1
        assert add(0, 5) == 5
        assert add(0, -1) == -1
        assert add(0, -10) == -10

    def test_add_anything_with_zero(self):
        assert add(1, 0) == 1
        assert add(5, 0) == 5
        assert add(-1, 0) == -1
        assert add(-10, 0) == -10

    def test_add_with_positive_values(self):
        assert add(1001, 203) == 1204
        assert add(59, 6) == 65

    def test_add_with_negative_values(self):
        assert add(-1009, -203) == -1212
        assert add(-59, -6) == -65

    def test_add_with_positive_and_negative_values(self):
        assert add(-1009, 203) == -806
        assert add(53, -9) == 44

