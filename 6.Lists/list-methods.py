# list methods does function in-place, it performs function directly on the list instead of returning a new list
spam = ['hello', 'hi', 'how', 'are', 'you']

# index() - returns the index of the value
print(spam.index('hi'))
# When try to find index of a value which is not in the list. It throws a ValueError. So this must be handled.
# print(spam.index('howdy'))

# append() - adds a value at the end of the list
print('Before Appending : ', spam)
spam.append('Howdy')
print('After Appending : ', spam)

# insert(index_to_insert, value_to_insert) - adds a value at the specified position of the list
print('Before Inserting : ', spam)
spam.insert(0, 'fuck')
print('After Inserting : ', spam)

# remove(value_to_remove) - removes the value from the list If present. If not present throws error
print('Before Removing : ', spam)
spam.remove('fuck')
print('After Removing : ', spam)
# if a particular is present multiple times(duplicate), it will only remove the first value

# sort() - sorts the list in ascending order. It sorts if list that contains numbers or strings.
print('Before Sorting : ', spam)
spam.sort()
print('After Sorting : ', spam)
# To sort in descending order, use ***sort(reverse=True)***
print('Before Reverse Sorting : ', spam)
spam.sort(reverse=True)
print('After Reverse Sorting : ', spam)
# You cannot sort a list having both numbers & strings eg. list = ['hello', 1, 10, 'back']
# sort() uses ASCII sorting.
# sort(key) - sorting is also possible based on the key value specified inside the function
spam.sort(key=str.lower)
print(spam)

