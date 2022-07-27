

from math import sqrt

lowest_Interval = int(input("Beginning of interval: "))
highest_Interval = int(input("End of interval: "))


# Return all prime numbers between the specified range
def get_all_primes_between(lowest_Interval:int, highest_Interval:int) -> list:

    primes = []

    for i in range(lowest_Interval, highest_Interval + 1):
        if is_prime(i):
            primes.append(i)
    
    return primes

# Function to tell whether a number is prime or not
def is_prime(number:int) -> bool:

    for divisor in range(2, int(sqrt(number))):
        if number % divisor == 0:
            return False

    return True

print(get_all_primes_between(lowest_Interval, highest_Interval))
