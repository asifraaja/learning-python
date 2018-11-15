# for-loop : iterate for a specific number of times

### it uses a range() function
# range(totalRange) where totalRange = Number of times you want to iterate. initialValue = 0 maxValue = totalRange
# range(startValue, endValue) = start from startValue and increase by 1 until endValue
# range(startValue, endValue, increaseByValue) = start from startValue and goto endValue with increment of increseByValue


# a simple-for
print('simple - for')
for i in range(5) :
    print(i)

print('for with start & end values')
# for with start & end values
for i in range(3, 6) :
    print (i)

print('for with a different increament value')
# for with a different increament value
for i in range(1, 6, 2) :
    print (i)

# a decreasing for
print('A decresing for statemet')
for i in range(10, 0, -2) :
    print (i)

