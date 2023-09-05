# Task 3

# One way to improve the quicksort is to use an insertion sort on lists that are
# small in length (call it the partition limit). Why does this make sense? Re-implement
# the quicksort and use it to sort a random list of integers. Perform analysis using
# different list sizes for the partition limit.

from random import randint

def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value

def quick_sort(array, partition_lim):
    if len(array) <= partition_lim:
        insertion_sort(array)
    else:
        quick_sort_helper(array, 0, len(array) - 1, partition_lim)


def quick_sort_helper(array, first, last, partition_lim):
    if first < last:
        split_point = partition(array, first, last)

        if split_point - first <= partition_lim:
            insertion_sort(array[first:split_point])
        else:
            quick_sort_helper(array, first, split_point - 1, partition_lim)

        if last - split_point <= partition_lim:
            insertion_sort(array[split_point + 1:last + 1])
        else:
            quick_sort_helper(array, split_point + 1, last, partition_lim)

def partition(array, first, last):
    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp

    return right_mark



test_list = [randint(1, 100) for _ in range(23)]
copy_test_list = test_list.copy()
quick_sort(copy_test_list, partition_lim=10)
print(copy_test_list)
