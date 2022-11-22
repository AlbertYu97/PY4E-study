"""
Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. But how would you determine 
that? How would you produce the list of all the words that Shakespeare used? 
Would you download all his work, read it and track all unique words by hand
"""

f_name = input('Enter file name:')
try:
    file = open(f_name)
except:
    print('File', f_name, 'does not exist.')
wordlist = list()
# For each line, sepearate the words by space
for line in file:
    words = line.split()
    # For each word, check if it exists in the word list. If not, add it.
    for word in words:
        if word not in wordlist:
            wordlist.append(word)
wordlist.sort()
print(wordlist)


"""
Exercise 5: Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection of 
emails. This was used by early email servers and desktop apps. Without getting 
into too many details, MBOX is a text file, which stores emails consecutively. 
Emails are separated by a special line which starts with From (notice the space). 
Importantly, lines starting with From: (notice the colon) describes the email 
itself and does not act as a separator. Imagine you wrote a minimalist email 
app, that lists the email of the senders in the user’s Inbox and counts the 
number of emails.
Write a program to read through the mail box data and when you find line that 
starts with “From”, you will split the line into words using the split function. 
We are interested in who sent the message, which is the second word on the From 
line.
"""

f_name = input('Enter file name:')
try:
    file = open(f_name)
except:
    print('File', f_name, 'does not exist')
    exit()
count = 0
for line in file:
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    count+=1
print('There were', count, 'lines in the file with From as the first word')


"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers and 
prints out the maximum and minimum of the numbers at the end when the user 
enters “done”. Write the program to store the numbers the user enters in a list 
and use the max() and min() functions to compute the maximum and minimum numbers 
after the loop completes."""
max,min = None, None
while True:
    value = input('Enter an interger:')
    if value == 'done':
        break
    try:
        value = int(value)
    except:
        print('input should be integer')
        continue
    if max is None:
        max = value
    if min is None:
        min = value
    elif max < value:
        max = value
    elif min > value:
        min = value
print('Max', max, 'Min', min)        