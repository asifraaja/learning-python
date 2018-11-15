# user-defined functions
# Functions are used to do sub-task
# Functions reduces resuablity of code
# Functions provide better reading of code

def myFirstFunction() :
    print('This is my first python function')
    print('Function always starts with "def"')
    print('This is the body of the function')
    print('This only defines a function. It is not executed until it is called')

# function that finds number which greater among three numbers
def findGreatestNumber(a, b, c) :
    print('The numbers are : ' + str(a) + " , " + str(b) + " and " + str(c))
    if (a > b) and (a > c):
        return a    # return statements. Returns the value from this function to calling function
    if(b > c):
        return b
    return c

# function that finds number which smallest among three numbers
def findSmallestNumber(a, b, c) :
    print('The numbers are : ' + str(a) + " , " + str(b) + " and " + str(c))
    if (a < b) and (a < c) :
        return a
    if (b < c):
        return b
    return c

# function that gives length of the largest string
def findLargestString(a, b, c):
    print('The Strings are : ' + str(a) + " , " + str(b) + " and " + str(c))
    aLen = len(a)   # len(a) = function that "returns length of string"
    bLen = len(b)
    cLen = len(c)
    return findGreatestNumber(aLen, bLen, cLen) # resuablity of the existing user-defined function

a = 'Mohamad Asif'
b = 'Vimal Prasaath'
c = 'Keerthi Avittan'
print('The largest string has ' + str(findLargestString(a, b, c)) + ' letters')