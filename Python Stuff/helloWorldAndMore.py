# This program says hello and asks for the user's name.
import time
from datetime import date
print('Hello World!')
print('What is your name?')     # ask for their name
myName = input()    # Capture name input into myName variable
print('It is good to meet you, ' + myName + '.')    # uses myName to be more specific
print('The length of your name is:')
print(len(myName))  # uses len() to find the lenghth of myName
print('What is your age?')  # ask for their age

while True:     # checks to make sure age is an integer
    try:
        myAge = int(input())     # Capture age input into myAge variable
    except ValueError:
        print('Please enter an age:')

    else:
        break

print('You will be ' + str(int(myAge) + 1) + ' in one year.')     # adds one to myAge and prints it

# I want to add datetime stuff to this program
# It could make for more accurate and specific outputs with myAge
# Thinking about using datetime class
today = date.today()
print("Today's date in ISO 8601 format:")
print(today)
# next idea is to ask for their birthday and tell how many days till their next one
