Task 2
Create a python program named "task2", and use the built-in function 'print' in it several times.
Try to pass "sep", "end" params and pass several parameters separated by commas.
Also, provide a comment text above each print statement, mentioned above,
with the expected output after execution of the particular print statement.

(Ex.
# 'hello world'
print("hello world")
)

Pay attention that usage of spaces is forbidden, as well as creating the whole result
text string using """ """, use '\n' and '\t' symbols instead.

#The print function should output the days of the week to the terminal and replace the spaces
# between the words with a non-"--" sign
#Sunday--Monday--Tuesday--Wednesday--Thursday--Friday--Saturday
print("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", sep="--")

#The print function should output the days of the week to the terminal and replace the spaces
# between the words with a non-"--" sign. And also add the line "--Days of the week" at the end of the line
#Sunday--Monday--Tuesday--Wednesday--Thursday--Friday--Saturday--Days of the week
print("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", sep="--",end="--Days of the week")
