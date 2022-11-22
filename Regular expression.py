
"""
Exercise 1: Write a simple program to simulate the operation of the grep 
command on Unix. Ask the user to enter a regular expression and count the 
number of lines that matched the regular expression:
"""

reg_exp = input('Enter a regular expression:')
file_name = input('Enter a file name:')
if len(file_name)<1:
    file_name = 'mbox.txt'
file = open(file_name)
count = 0
import re
for line in file:
    line = line.rstrip()
    if re.search(reg_exp, line):
        count+=1
print(file_name, 'has',count, 'lines that matched', reg_exp)


"""
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression and the 
findall() method. Compute the average of the numbers and print out the average 
as an integer.
"""

file_name = input('Enter a file name:')
if len(file_name)<1:
    file_name = 'mbox.txt'
file = open(file_name)
count = 0
sum = 0
import re
for line in file:
    line = line.rstrip()
    # Find everthing that starts with 'New Revision: ' and a interger then only
    # return the integer
    x =  re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        for version in x:
            number = int(version)
            count+=1
            sum += number
print(int(sum/count))
