"Using timeit to measure the performance of string concatenation"
import timeit

str = 'Using timeit to measure the performance of string concatenation'
strs = str.split(' ') * 5
print strs

setup = "from __main__ import strs"

statements = ["""\
str2 = ''
for s in strs:
    str2 += s
""",
"""\
str2 = ''
str2 = ''.join(strs)
"""]

def test(st):
    t = timeit.Timer(st, setup)
    times = t.repeat(3)
    print times

for i, st in enumerate(statements):
    print 'Method %d:' % (i + 1)
    test(st)
