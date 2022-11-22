"""
Exercise 2: Write a program that categorizes each mail message by which day 
of the week the commit was done. To do this look for lines that start with 
“From”, then look for the third word and keep a running count of each of the 
days of the week. At the end of the program print out the contents of your 
dictionary (order does not matter).
"""

frequency = dict()
f_name = input('Enter file name:')
try:
    file = open(f_name)
except:
    print('File', f_name, 'does not exist.')
    exit()
for line in file:
    words = line.split()
    if not line.startswith('From ') or len(words) < 3:
        continue    
    date = words[2]
    frequency[date] = frequency.get(date,0) + 1
print(frequency)

"""
Exercise 3: Write a program to read through a mail log, build a histogram 
using a dictionary to count how many messages have come from each email 
address, and print the dictionary.
"""

email = dict()
file = input('Enter file name:')
if len(file) <1:
    file = 'mbox-short.txt'
file = open(file)

for line in file:
    words = line.split()
    if not line.startswith('From ') or len(words) < 3:
        continue 
    address = words[1]
    email[address] = email.get(address,0) +1
# .items() send the dictonary into tuples, a pair of key & value in each tuple
for address, number in email.items():
    print(address, number)


"""
Exercise 4: Add code to the above program to figure out who has the most 
messages in the file. After all the data has been read and the dictionary 
has been created, look through the dictionary using a maximum loop  to 
find who has the most messages and print how many messages the person has.
"""

email = dict()
file = input('Enter file name:')
if len(file) <1:
    file = 'mbox-short.txt'
file = open(file)

for line in file:
    words = line.split()
    if not line.startswith('From ') or len(words) < 3:
        continue 
    address = words[1]
    email[address] = email.get(address,0) +1
max = 0
add = None
for address, number in email.items():
    if number > max:
        add = address
        max = number
print(add, max)
"""


Exercise 5: This program records the domain name (instead of the address) 
the message was sent from instead of who the mail came from (i.e., the whole 
email address). At the end of the program, print out the contents of your 
dictionary.
"""
email = dict()
file = input('Enter file name:')
if len(file) <1:
    file = 'mbox-short.txt'
file = open(file)

for line in file:
    words = line.split()
    if not line.startswith('From ') or len(words) < 3:
        continue 
    address = words[1]
    domain = address.split('@')
    domain_name = domain[1]
    email[domain_name] = email.get(domain_name,0) +1
# .items() send the dictonary into tuples, a pair of key & value in each tuple
for address, number in email.items():
    print(address, number)