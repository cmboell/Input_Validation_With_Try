"""
Assignment name: Basic Input and Format Output Assignment
Program: average_scores.py
Author: Colby Boell
Last date modified: 01/19/2022

The purpose of this program is to prompt user for their first name, last name, age
and 3 different test score values out of 100. Then take the 3 scores and find the average to store in a variable,
then print out the user first and last name, age, and average score (formatted 2 decimal places) as a
formatted sentence.
"""

import constants

# prompt user input for first name / this displays prompt and takes the input
first_name = input('Please enter your first name: ')
# prompt user input for last name / this displays prompt and takes the input
last_name = input('Please enter your last name: ')

# prompt user for input/ this displays prompt and takes input
age = int(input('Enter your age: '))

# prompts user for test scores/ they display prompt and take input
first_test_score = int(input('Enter first test score: '))
second_test_score = int(input('Enter second test score: '))
third_test_score = int(input('Enter third test score: '))


# variable to hold average test score out of all 3 scores using a constant from constants file
average_grade = (first_test_score + second_test_score + third_test_score) / constants.NUMBER_OF_TESTS

# prints formatted results as a string
print(f'{last_name.capitalize()}, {first_name.capitalize()} Age: {age} Average Grade: {average_grade: 5.2f}')

""""
observed output for cOLBY bOeLl 33 89 98 100 :
Boell, Colby Age: 33 average grade  95.67

observed output for lisa kellihan 40 90 70 80 :
Kellihan, Lisa Age: 40 Average Grade:  80.00
"""
