# Task 1

# Practice asynchronous code

# Create a separate asynchronous code to calculate Fibonacci,
# factorial, squares and cubic for an input number. Schedule
# the execution of this code using asyncio.gather for a list
# of integers from 1 to 10. You need to get four lists of
# results from corresponding functions.

# Rewrite the code to use simple functions to get the same
# results but using a multiprocessing library. Time the
# execution of both realizations, explore the results,
# what realization is more effective, why did you get a
# result like this.

import asyncio
import multiprocessing
import time


async def async_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return await async_fibonacci(n - 1) + await async_fibonacci(n - 2)


async def async_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result


async def async_list_squares(a, b):
    square_list = []
    for count in range(a, b + 1):
        square_list.append(count**2)
    return square_list


async def async_list_cubes(a, b):
    cube_list = []
    for count in range(a, b + 1):
        cube_list.append(count**3)
    return cube_list


async def async_calculate(num):
    fibonacci_result = await async_fibonacci(num)
    factorial_result = await async_factorial(num)
    squares_result = await async_list_squares(1, num)
    cubes_result = await async_list_cubes(1, num)
    return (fibonacci_result, factorial_result, squares_result, cubes_result)


def multiprocess_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return multiprocess_fibonacci(n - 1) + multiprocess_fibonacci(n - 2)


def multiprocess_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result


def multiprocess_list_squares(a, b):
    square_list = []
    for count in range(a, b + 1):
        square_list.append(count**2)
    return square_list


def multiprocess_list_cubes(a, b):
    cube_list = []
    for count in range(a, b + 1):
        cube_list.append(count**3)
    return cube_list


def multiprocess_calculate(num):
    fibonacci_result = multiprocess_fibonacci(num)
    factorial_result = multiprocess_factorial(num)
    squares_result = multiprocess_list_squares(1, num)
    cubes_result = multiprocess_list_cubes(1, num)
    return (fibonacci_result, factorial_result, squares_result, cubes_result)


async def async_main():
    async_tasks = [async_calculate(i) for i in range(1, 11)]
    async_results = await asyncio.gather(*async_tasks)
    return async_results


def multiprocess_main():
    with multiprocessing.Pool(processes=4) as pool:
        multiprocess_results = pool.map(multiprocess_calculate, range(1, 11))
    return multiprocess_results


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(async_main())
    print("ASYNC TIME", time.time() - start_time)

    start_time = time.time()
    multiprocess_main()
    print("MULTIPROCESSING TIME:", time.time() - start_time)
