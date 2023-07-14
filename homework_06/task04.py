# Task 4

# Create a list of days of the week.
# In one line (or as usual) create a dictionary
# of the form: {1: "Monday", 2:...
# Also, in one line or as usual, create a reverse
# dictionary {"Monday": 1,

list_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

res = []
for index, elem in enumerate(list_week):
    res.append((elem, index+1))
print(dict(res))

res = []
for index, elem in enumerate(list_week):
    res.append((index+1, elem))
print(dict(res))
