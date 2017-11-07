# This program says hello and asks for the user's name.
print('Hello World!')
print('What is your name?')     # ask for their name
myName = input()    # Capture name input into myName variable
print('It is good to meet you, ' + myName + '.')    # uses myName to be more specific
print('The length of your name is:')
print(len(myName))  # uses len() to find the lenghth of myName
print('What is your age?')  # ask for their age
myAge = input()     # Capture age input into myAge variable
print('You will be ' + str(int(myAge) + 1) + ' in one year.')     # adds one to myAge and prints it

# I want to add datetime stuff to this program
# It could make for more accurate and specific outputs with myAge
# Thinking about using datetime class
