import logging

logging.basicConfig(level=logging.DEBUG)

def log_args(func):
    log = logging.getLogger('ArgsLogger')
    log.setLevel(logging.DEBUG)
    def log_args_inner(*args, **kwargs):
        log.debug(func.__name__ + ' called with args:' + str(args) + ' and keyword args: ' + str(kwargs))
        ret = func(*args, **kwargs)
        log.debug(func.__name__ + ' returned ' + str(ret))
    return log_args_inner

def add(x, y):
    return x + y

add = log_args(add)

if __name__ == "__main__":
    print "add(5, 4):"
    add(5, 4)
    print "add(5, y=4):"
    add(5, y=4)
