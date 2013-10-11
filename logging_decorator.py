import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('ArgsLogger')
log.setLevel(logging.DEBUG)

def log_args(func):
    def log_args_inner(*args, **kwargs):
        log.debug(func.__name__ + ' called with args:' + str(args) + ' and keyword args: ' + str(kwargs))
        ret = func(*args, **kwargs)
        log.debug(func.__name__ + ' returned ' + str(ret))
    return log_args_inner

def add(x, y):
    return x + y

def add3(x, y, z):
    return x + y + z

add = log_args(add)
add3 = log_args(add3)

if __name__ == "__main__":
    log.debug("add(5, 4):")
    add(5, 4)
    log.debug("add(5, y=4):")
    add(5, y=4)
    log.debug("add3(5, 4, 2):")
    add3(5, 4, 2)
    log.debug("add3(5, y=4, z=2):")
    add3(5, y=4, z=2)
