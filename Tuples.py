"""
Exercise 1: Revise a previous program as follows: Read and parse the “From” 
lines and pull out the addresses from the line. Count the number of messages 
from each person using a dictionary.

After all the data has been read, print the person with the most commits by 
creating a list of (count, email) tuples from the dictionary. Then sort the 
list in reverse order and print out the person who has the most commits.
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
# Creat a empty list
tmp = list()
# Change the order of address and number of occurence
for add, num in email.items():
    tmp.append((num, add))
# sort the list in descending order
tmp_sorted = sorted(tmp, reverse = True)
tmp2 = list()
for num, add in tmp_sorted:
    tmp2.append((add, num))
# Return the 1st element
print(tmp2[0])


"""
Exercise 2: This program counts the distribution of the hour of the day for 
each of the messages. You can pull the hour from the “From” line by finding 
the time string and then splitting that string into parts using the colon 
character. Once you have accumulated the counts for each hour, print out the 
counts, one per line, sorted by hour as shown below.
"""

timefreq = dict()
file = input('Enter file name:')
if len(file) <1:
    file = 'mbox-short.txt'
file = open(file)

for line in file:
    words = line.split()
    if not line.startswith('From ') or len(words) < 3:
        continue 
    time = words[5]
    time_split = time.split(':')
    # select the 1st element - hour
    hour = time_split[0]
    timefreq[hour] = timefreq.get(hour,0) +1
print(timefreq)
lst = list()
for hour, num in timefreq.items():
    lst.append((num, hour))
print(lst)
lst = sorted(lst, reverse = True)
for num, hour in lst:
    print(hour, num)


"""
Exercise 3: Write a program that reads a file and prints the letters in 
decreasing order of frequency. Your program should convert all the input to 
lower case and only count the letters a-z. Your program should not count spaces,
digits, punctuation, or anything other than the letters a-z. Find text samples 
from several different languages and see how letter frequency varies between 
languages. Compare your results with the tables at 
https://wikipedia.org/wiki/Letter_frequencies.
"""
import string
file = input('Enter file name:')
if len(file) <1:
    file = 'mbox-short.txt'
file = open(file)

freq = dict()
for line in file:
    # Delete spaces on the right
    line = line.rstrip()
    # Delete all the spaces, digits etc
    line = line.translate(line.maketrans('','', string.punctuation))
    # convert to all lower cases
    line = line.lower()
    # store in the dictionary
    words = line.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            freq[letter] = freq.get(letter,0) +1
freq_sorted = sorted(freq.items())
print(freq_sorted)