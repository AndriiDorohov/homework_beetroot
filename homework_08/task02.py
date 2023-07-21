# Task 2

# The sys module.

#  The “sys.path” list is initialized from the
# PYTHONPATH environment variable. Is it possible
# to change it from within Python? If so, does it
# affect where Python looks for module files? Run
# some interactive tests to find it out.

import os
import sys

list_path = []
mod_path = []

for p in sys.path:
    list_path.append(p)
    print(p)

sys.path.insert(0, os.path.abspath(str(os.getcwd()) + "/modules"))

for p in sys.path:
    mod_path.append(p)

for p in mod_path:
     if p not in list_path:
           print('was added new path: ' + p)
