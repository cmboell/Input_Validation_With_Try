"""
Assignment name: Input Validation with Try Assignment
Program: average_scores.py
Author: Colby Boell
Last date modified: 02/02/2022

The purpose of this program is to prompt user for their first name, last name, age
and 3 different test score values out of 100. Then take the 3 scores and find the average to store in a variable,
then print out the user first and last name, age, and average score (formatted 2 decimal places) as a
formatted sentence.
---With try statements
"""
import constants

# prompt user input for first name / this displays prompt and takes the input
first_name = input('Please enter your first name: ')
# prompt user input for last name / this displays prompt and takes the input
last_name = input('Please enter your last name: ')

# prompt user for input/ this displays prompt and takes input, try input validation for age
try:
    age = int(input('Enter your age: '))
    if age >= 0:
        print('Valid age', end=', ')
    else:
        print('invalid')
except:
    age = 0
    print('Age invalid', end=', ')
else:
    print('Basic information recorded')
finally:
    print('Now enter your scores')

# prompts user for test scores/ they display prompt and take input
# first test score try for input validation
try:
    first_test_score = int(input('Enter first test score: '))
    if first_test_score >= 0:
        print('Score recorded', end=', ')
    else:
        print('invalid')
except:
    first_test_score = 0
    print('no score recorded', end=',d ')
finally:
    print('Next score')
# input for second score and try for input validation
try:
    second_test_score = int(input('Enter second test score: '))
    if second_test_score >= 0:
        print('Score recorded', end=', ')
    else:
        print('invalid')
except:
    second_test_score = 0
    print('no score recorded', end=', ')
finally:
    print('Next score')
# input for test 3 and try input validation
try:
    third_test_score = int(input('Enter third test score: '))
    if third_test_score >= 0:
        print('Score recorded', end=', ')
    else:
        print('invalid')
except:
    third_test_score = 0
    print('no score recorded', end=', ')
finally:
    print('Next score')

# variable to hold average test score out of all 3 scores using a constant from constants file
average_grade = (first_test_score + second_test_score + third_test_score) / constants.NUMBER_OF_TESTS

# prints formatted results as a string
print(f'{last_name.capitalize()}, {first_name.capitalize()} Age: {age} Average Grade: {average_grade: 5.2f}')

""""
Tests: 
1.)                                    
Please enter your first name: t
Please enter your last name: t
Enter your age: t
Age invalid, Now enter your scores
Enter first test score: t
no score recorded, Next score
Enter second test score: t
no score recorded, Next score
Enter third test score: t
no score recorded,d Next score
T, T Age: 0 Average Grade:  0.00

2.)
Please enter your first name: colby
Please enter your last name: BoEll
Enter your age: 33
Valid age, Basic information recorded
Now enter your scores
Enter first test score: 67
Score recorded, Next score
Enter second test score: 88
Score recorded, Next score
Enter third test score: 92
no score recorded, Next score
Boell, Colby Age: 33 Average Grade:  51.67
"""
