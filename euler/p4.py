# coding=utf-8
"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
comment = \
"""
    999 999 = x
    999 998
    999 997
    ...
    999 500
    999 499
    ...
    999 3
    999 2
    999 1

    998 998
    998 997
    998 996
"""

def is_palindrome(x):
    x = str(x)
    y = x[::-1]
    return x == y

def test_is_palindrome():
    assert is_palindrome("abba")
    assert is_palindrome("madam")
    assert is_palindrome("malayalam")
    assert not is_palindrome("abcd")
    assert is_palindrome("1001")
    assert is_palindrome("101")
    assert not is_palindrome("1011")

def find_greatest():
    palindrome = None
    for x in range(999, 100, -1):
        val = x * 999
        if palindrome and palindrome[2] > val:
            print 'quitting x loop at', x
            break
        for y in range(999, 100, -1):
            val = x * y
            if palindrome and palindrome[2] > val:
                print 'quitting y loop at', y
                break
            if is_palindrome(val):
                palindrome = (x, y, val)
    return palindrome


def p():
    print find_greatest()

p()