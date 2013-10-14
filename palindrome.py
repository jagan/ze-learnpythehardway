def is_palindrome(x):
    x = str(x)
    _len = len(x)
    for i in range(_len/2):
        print 'i=', i, ' | comparing', x[i], 'and', x[_len-1-i]
        if x[i] != x[_len-1-i]:
            return False
    return True

def is_palindrome2(x):
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
