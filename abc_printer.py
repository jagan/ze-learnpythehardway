"""
Demonstrating Abstract Base Classes using various printers
"""
import abc

class AbstractPrinter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def print_data(self, data):
        print 'I am an Abstract Printer. I do not know how to print stuff.'

    @abc.abstractproperty
    def is_color(self):
        return False

class DotMatrixPrinter(AbstractPrinter):
    def print_data(self, data):
        print '.' * 100
        print data
        print '.' * 100

    def is_color(self):
        return False

class InkJetPrinter(AbstractPrinter):
    def print_data(self, data):
        print '*' * 100
        print data
        print '*' * 100

    @property
    def is_color(self):
        return True

class LaserPrinter(object):
    'Not sub-classing AbstractPrinter'

    def print_data(self, data):
        print '_' * 100
        print data
        print '_' * 100

    @property
    def is_color(self):
        return False

AbstractPrinter.register(LaserPrinter)

class AlienPrinter(object):
    def qwerty(self):
        print 'quacky!'

def p():
    assert issubclass(DotMatrixPrinter, AbstractPrinter)
    assert issubclass(InkJetPrinter, AbstractPrinter)
    assert issubclass(LaserPrinter, AbstractPrinter)
    assert not issubclass(AlienPrinter, AbstractPrinter)

    assert isinstance(DotMatrixPrinter(), AbstractPrinter)
    assert isinstance(InkJetPrinter(), AbstractPrinter)
    assert isinstance(LaserPrinter(), AbstractPrinter)
    assert not isinstance(AlienPrinter(), AbstractPrinter)

    printers = [DotMatrixPrinter(), InkJetPrinter(), LaserPrinter()]
    for printer in printers:
        print 'Printing using %s:' % printer.__class__.__name__
        printer.print_data('QWERTYUIOP{}|\tSDFGHJKL:"\tZXCVBNM<>?\t\t' * 2)
        print


if __name__ == "__main__":
    p()