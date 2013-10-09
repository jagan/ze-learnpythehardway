len = 91
half = len / 2
for i in range(0, half + 1):
    for j in range(1, len):
        if (j > half - i) and (j < half + i):
            print str(unichr(ord('a') + (abs(j - half) % 26))),
        else:
            print ' ',
    print
