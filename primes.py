"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Only positive inputs are allowed")
    
    list = []
    number = 2
    while len(list) < number_of_primes:
        if is_prime(number):
            list.append(number)
        number = number + 1
    return list