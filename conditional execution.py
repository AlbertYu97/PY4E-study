# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the 
# hourly rate for hours worked above 40 hours.
Hours = input('Enter Hours: ')
Rate = input ('Enter Rate: ')
h = float(Hours)
r = float(Rate)
if int(Hours) > 40:
    print("Overtime")
    reg = h*r
    otp = (h-40)*0.5*r
    pay = reg+otp
else:
    print('Regular')
    pay = h*r
print('Pay:',pay)
 

# Exercise 2: Rewrite your pay program using try and except so that your program 
# handles non-numeric input gracefully by printing a message and exiting the 
# program. The following shows two executions of the program:

Hours = input('Enter Hours: ')
try: 
    h = float(Hours)
except:
    print('Error, please enter numeric input')
    # If something is wrong, quit and do not run codes below
    quit()
Rate = input ('Enter Rate: ')
try: 
    r = float(Rate)
except:
    print('Error, please enter numeric input')
    quit()
# Determine work overtime    
if h > 40:
    print("Overtime")
    reg = h*r
    otp = (h-40)*0.5*r
    pay = reg+otp
else:
    print('Regular')
    pay = h*r
print('Pay:',pay)

# Exercide 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. If the score is 
# between 0.0 and 1.0, print a grade using the following table:
score = input('Enter Score: ')
try:
    score = float(score)
except:
    print('Bad score')
    quit()
if score>1 or score<0:
    print('Error! You must enter a score between 0.0 and 1.0')
    quit()
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
