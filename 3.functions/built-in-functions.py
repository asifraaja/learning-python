# python has a wide range of built-in functions.
# For eg : print(), str(), bool(), input()

# We can use other funtions by just import them

# Importing the randint() function 
import random, sys

randomNum = random.randint(1, 5)
print(randomNum)

# Using randint() + while loop
while randomNum != 5 :
    randomNum = random.randint(1, 5)
    print(randomNum)

# We can also use 3rd party functions. We can download the libraries using pip command
# pip install "3rd party module"

# Using sys.exit() function = It stops the execution of the program
sys.exit()

print('Exiting') # This line will never be executed as the program exits above
