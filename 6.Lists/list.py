# List is a data structure.
# [1, 2, 3]

# similar to array in other programming languages

fruits = ['apple', 'banana', 'custard', 'kiwi']

print(fruits)
print(fruits[-1])
print(fruits[2:])   # This is slice operation
fruits[2] = 'papaya'
print(fruits)
print('Length of fruits : ', len(fruits)) # This is len() operation
del fruits[1] # removes the value from the list
print(fruits)

fruits2 = ['starfruit', 'watermelon']
combined_fruits = fruits + fruits2 # list concatenation
print(combined_fruits)

is_apple_in_list = 'apple' in fruits # checks if a data is in a list # not in checks if an item is not in
print(is_apple_in_list)