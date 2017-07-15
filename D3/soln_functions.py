# Create a function with the following characteristics:
# Name the function: myprinter
# For this exercise, don't worry about accepting arguments, just include your name and age in the body of the function
# Have the function print your name
# Have the function print your age
# Test the function, by calling it

def myprinter():
    age = 42
    name = 'batman'
    print(name)
    print(age)

myprinter()





# Create a function with the following characteristics:
# Name the function: mysport
# Have the function accept one argument: fav_sport
# Have the function print your favorite sport
# Test the function, by calling it, with an argument

def mysport(fav_sport):
    print(fav_sport)

mysport('parkour')



# Create a function with the following characteristics:
# Name the function: myfavorites
# Have the function accept two arguments: fav_food & fav_animal
# Have the function print your favorite food
# Have the function print your favorite animal
# Test the function, by calling it, with two arguments

def myfavorites(fav_food, fav_animal):
    print(fav_food)
    print(fav_animal)

myfavorites('sushi', 'lemur')



# Create a function with the following characteristics:
# Name the function: defaultfavorites
# Have the function accept two arguments: fav_food & fav_animal
# Assign a default value for favorite animal of 'raccoon'
# Have the function print your favorite food and your favorite animal
# Test the function, by calling it, both with and without an argument for the favorite animal


def defaultfavorites(fav_food, fav_animal='raccoon'):
    print(fav_food)
    print(fav_animal)

defaultfavorites('sushi', 'orangutan')

defaultfavorites('sushi')



# if / elif / else
# Create an if statement
# Your if statement should test to see if a variable is equal to a specific value
# Create a variable called name and assign it to a string of your name
# Use an if statement to test whether name is equal to a string of your name
# IF they are equal, print: "the name variable is equal to the string"
# Use an if statement to test whether name is equal to a string that is NOT your name
# This should fail >>> you don't need to do anything in this case.

name = 'diana prince'

if name == 'diana prince':
    print('the name variable is equal to the string')

if name == 'selina kyle':
    print('the name variable WAS NOT equal to the string')



# for loops
# Create a for loop
# Your for loop should do the following:
# use each item in a list of 10 integers (i.e. [1, 13, 42, 2001, ...])
# multiply each item by 10 and save that value as a separate variable called multiple
# print both the value of each item and the value of multiple

# Your for loop should do the following:
# use each item in a list of 10 strings (i.e. ['a', 'b', 'd', 'x', ...])
# display.show() each item on the micro:bit screen

for num in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]:
    multiple = num * 10
    print(num, multiple)


for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
    display.show(letter)

# while loops
# Create a while loop
# Your while loop should do the following:
# Use the True keyword so that the loop runs forever (or is told to stop)
# print() the micro:bit's temperature
# check to see if button_a was pressed
# if button_a was pressed:
#     display.show() the letter 'X'
#     break out of the while loop

while True:
    print(temperature)
    if button_a.was_pressed():
        display.show()
        break
