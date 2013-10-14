import random

def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)

def consume():
    """Displays a running average across lists of integers sent to it"""
    print 'inside consume'
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print 'The running average is ', running_sum / float(data_items_seen)

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer
    function"""
    while True:
        data = get_data()
        print 'Produced ', data
        consumer.send(data)
        yield

if __name__ == '__main__':
    print 1
    consumer = consume()
    print 3
    consumer.send(None)
    print 'after send'
    producer = produce(consumer)

    for _ in range(10):
        print('Producing...')
        next(producer)
