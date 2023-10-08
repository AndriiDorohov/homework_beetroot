# Програма мінімум:

# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

# Прочитати про Fibonacci search та імплементуйте його за допомогою
# Python. Визначте складність алгоритму та порівняйте його з бінарним
# пошуком

# Середній рівень:


from bisect import bisect_left
import timeit


def binary_search_recursive(items, value, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if items[mid] == value:
        return True
    elif items[mid] < value:
        return binary_search_recursive(items, value, mid + 1, high)
    else:
        return binary_search_recursive(items, value, low, mid - 1)


def fibMonaccianSearch(items, value, high):
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1

    while fibM < high:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while fibM > 1:
        i = min(offset + fibMMm2, high - 1)

        if items[i] < value:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif items[i] > value:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            # return i
            return True

    if fibMMm1 and items[high - 1] == value:
        return high - 1

    return -1


def search(items, value, search_method):
    if search_method == "binary":
        low = 0
        high = len(items) - 1
        found = binary_search_recursive(items, value, low, high)
    elif search_method == "fibonachi":
        high = len(items)
        found = fibMonaccianSearch(items, value, high)
    return found


if __name__ == "__main__":
    print("--------Operation of functions with a large list--------")
    bin_timer = timeit.timeit(
        stmt="search(list(range(200000)), 167000, 'binary')",
        number=100,
        setup="from __main__ import search",
    )

    fib_timer = timeit.timeit(
        stmt="search(list(range(200000)), 167000, 'fibonachi')",
        number=100,
        setup="from __main__ import search",
    )
    base_time = min(bin_timer, fib_timer)
    print("Binary:    {:.4f} seconds".format(bin_timer))
    print("Fibonacci: {:.4f} seconds".format(fib_timer))
    print("Difference: {:.2f}%".format(((fib_timer - bin_timer) / base_time) * 100))

    print("--------Operation of functions with a short list--------")
    bin_timer = timeit.timeit(
        stmt="search(list(range(20)), 16, 'binary')",
        number=400,
        setup="from __main__ import search",
    )

    fib_timer = timeit.timeit(
        stmt="search(list(range(20)), 16, 'fibonachi')",
        number=400,
        setup="from __main__ import search",
    )
    base_time = min(bin_timer, fib_timer)
    print("Binary:    {:.4f} seconds".format(bin_timer))
    print("Fibonacci: {:.4f} seconds".format(fib_timer))
    print("Difference: {:.2f}%".format(((fib_timer - bin_timer) / base_time) * 100))
