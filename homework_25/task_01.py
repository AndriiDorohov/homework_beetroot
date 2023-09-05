# Task 1

# A bubble sort can be modified to bubble in both directions. The first pass moves
# up the list and the second pass moves down. This alternating pattern continues
# until no more passes are necessary. Implement this variation and describe under
# what circumstances it might be appropriate.

from random import randint

def bubble_two_way(s_list):
    cond = True
    while cond:
        cond = False

        for i in range(0, len(s_list)-1):
            if s_list[i] > s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                cond = True

        for i in range(len(s_list)-1, 1, -1):
            if s_list[i] < s_list[i-1]:
                s_list[i], s_list[i-1] = s_list[i-y1], s_list[i]
                cond = True
    return s_list

n_list = []
for i in range(10):
    n_list.append(randint(1, 99))
print(f'New generated list:  {n_list}')
print(f'Sorted bubble two way method: {bubble_two_way(n_list)}')
