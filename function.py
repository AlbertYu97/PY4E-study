#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
#create a function called computepay which takes two parameters (hours and rate).
"""def computepay(hours, rate):
    if hours > 40:
        print('overtime')
        return hours*rate + (hours-40)*0.5*rate
    else:
        print('regular')
        return hours*rate
"""
# Exercise 7: Rewrite the grade program from the previous chapter using a 
# function called computegrade that takes a score as its parameter and returns 
#a grade as a string.
def computegrad(score):
    if score < 0 or score >1:
        print('Score has to between 0 to 1')
        exit()
    if score < 0.6:
        return 'F'
    elif score <0.7:
        return 'D'
    elif score <0.8:
        return 'C'
    elif score <0.9:
        return 'B'
    else:
        return 'A'
score = input('Enter score:')
try:
        score = float(score)
except:
        print('Score has to between a number from 0 to 1')
        exit()
grad = (computegrad(score))
print('Score is:',grad)
        