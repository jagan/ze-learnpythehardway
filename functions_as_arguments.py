import pytest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def func(x):
    assert 0 # fail unconditionally

def apply(func, x, y):
    return func(x, y)

def test_apply_with_add():
    res = apply(add, 5, 4)
    assert res == 9

def test_apply_with_sub():
    res = apply(sub, 5, 4)
    assert res == 1

def test_apply_with_less_arguments():
    with pytest.raises(TypeError):
        apply(func, 2, 7)