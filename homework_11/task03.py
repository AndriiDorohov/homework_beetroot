# Task 3

# Write a function called "choose_func" which takes a list of nums
# and 2 callback functions. If all nums inside the list are positive,
# execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

# def choose_func(nums: list, func1, func2):

#     pass

# # Assertions
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, -2, 3, -4, 5]

def choose_func(nums: list, func1, func2):
		if min(nums) >= 0:
						return func1(min(nums))
		else:
						return func2(min(nums))

def func_1(arg):
		return arg + 1

def func_2(arg):
		return arg + arg

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
result = choose_func(nums1, func_1, func_2)
print(result)
result = choose_func(nums2, func_1, func_2)
print(result)
