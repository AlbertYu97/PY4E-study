# Exercise 1: Write a program which repeatedly reads numbers until the user enter
#“done”. Once “done” is entered, print out the total, count, and average of the 
# numbers. If the user enters anything other than a number, detect their mistake 
# using try and except and print an error message and skip to the next number.
"""count=0
sum=0
while True:
    line = input('Enter a number:')
    if line == 'done':
        break
    try:
        line = float(line)
    except:
        continue
    else:
        count +=1
        sum +=line
print('total:',sum, 'Count:',count, 'Average:', sum/count)
"""
# Exercise 2: Write another program that prompts for a list of numbers as above 
#and at the end prints out both the maximum and minimum of the numbers instead 
#of the average.
max=None
min=None
while True:
    line = input('Enter a number:')
    if line == 'done':
        break
    try:
        line = float(line)
    except:
        print('Invalid Input')
        continue
    if max is None:
        max = line
    if min is None:
        min = line
    if line > max:
        max = line
    if line < min:
        min = line
print('max:',max, 'min',min)