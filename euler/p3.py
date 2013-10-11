'Largest prime factor'
import math

def primes():
    yield 2
    primes = [2]
    pot_prime = 3
    while True:
        sqrt_pot_prime = math.sqrt(pot_prime)
        is_prime = True
        for prime in primes:
            if prime > sqrt_pot_prime:
                break
            if pot_prime % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(pot_prime)
            print 'Returning prime', pot_prime, '|',
            yield pot_prime
        pot_prime += 2 # skip even numbers

def p(x):
    for prime in primes():
        if x <= prime:
            return prime
        while x % prime == 0 and x > prime:
            print
            print prime, 'is a factor'
            x /= prime
            print 'x is now', x
        if x <= prime:
            return x


x = p(600851475143)
print
print 'Largest prime factor is:', x
