# Task 1

# Primes

# NUMBERS = [
#    2,  # prime
#    1099726899285419,
#    1570341764013157,  # prime
#    1637027521802551,  # prime
#    1880450821379411,  # prime
#    1893530391196711,  # prime
#    2447109360961063,  # prime
#    3,  # prime
#    2772290760589219,  # prime
#    3033700317376073,  # prime
#    4350190374376723,
#    4350190491008389,  # prime
#    4350190491008390,
#    4350222956688319,
#    2447120421950803,
#    5,  # prime
# ]
# We have the following input list of numbers, some of them are prime.
# You need to create a utility function that takes as input a number and
# returns a bool, whether it is prime or not.


# Use ThreadPoolExecutor and ProcessPoolExecutor to create different
# concurrent implementations for filtering NUMBERS.

# Compare the results and performance of each of them.

import concurrent.futures
import math
import time

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def multiprocessing_func():
    start_time = 0
    end_time = 0
    print("MULTIPROCESSING START")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        start_time = time.time()
        for number, prime in zip(NUMBERS, executor.map(is_prime, NUMBERS)):
            print("%d is prime: %s" % (number, prime))
        end_time = time.time()
    print("Time: ", end_time - start_time)


def multithreading_func():
    start_time = 0
    end_time = 0
    print("MULTITHREADING START")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        for number, prime in zip(NUMBERS, executor.map(is_prime, NUMBERS)):
            print("%d is prime: %s" % (number, prime))
        end_time = time.time()
    print("Time: ", end_time - start_time)


if __name__ == "__main__":
    multiprocessing_func()
    multithreading_func()
