# ProjectEuler.net
# Problem7
# William Martin
# 2/22/2018

# What is the 10,001st prime number?

import time

# Find if a number is prime
def isPrime(n):
    # check for factors of 2 first
    if n % 2 == 0:
        return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0:
            return False
            p += 2
        return True

def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if isPrime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

# start = time.time()
# prime = nth_prime(1)
# elapsed = (time.time()- start)
#
# print("Found %s in %s seconds" %(prime, elapsed))


def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]
print(primes(10001))
