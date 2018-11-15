### Using try-catch block allows the program not to crash

def divide(a, b):
    print("Divide " + str(a) + " by " + str(b), end=':.  ')
    try :
        return a/b
    except ZeroDivisionError :
        return "Cannot Divide by Zero"

print(divide(45, 2))
print(divide(2, 0))
print(divide(3, 1))

def getMarks(a) :
    try :
        marks = int(a)
        if(marks >= 0) :
            print('Marks entered : ' + str(marks))
            return marks
    except ValueError :
        print('Mark must be a number >= 0')

while True :
    print('Please enter your marks')
    marks = getMarks(input())
    if(marks != None):
        break

