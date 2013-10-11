
def cells(height, width):
    for x in range(height):
        for y in range(width):
            yield (x, y)

def process_cell(x, y):
    print 'Processing cell [%d, %d]' % (x, y)

if __name__ == "__main__":
    for x, y in cells(20, 10):
        process_cell(x, y)
