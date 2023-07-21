# Task 1

# Imports practice

#  Make a directory with 2 modules; make a function
# in one of them; then import this function in the
# other module and use that in your script of choice.

import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
os.mkdir(cur_dir + "/test")
os.chdir(cur_dir + "/test")
print(os.getcwd())

with open('__init__.py', 'w') as file:
    L = ["print(f'Файл __init__.py в пакете {__name__}')"]
    file.writelines(L)

with open('module1.py', 'w') as file:
    L = ["def my_function(a, b): \n", "    return a+b \n"]
    file.writelines(L)

with open('module2.py', 'w') as file:
    L = ["from test.module1 import my_function \n", "print(my_function(105, 55)) \n"]
    file.writelines(L)

import test.module2
