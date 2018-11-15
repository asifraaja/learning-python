# This script describes the *** Similarities of List & String ***
convert_string_to_list = list('hello')  # converts string to list
print(convert_string_to_list)

simple_list = convert_string_to_list
print(simple_list)

print(simple_list[2])

# iterating a list similar to string
for letter in simple_list :
    print(letter)

# in & not in operations
print('o' in simple_list)
print('h' not in simple_list)

# slice operations
print(simple_list[:2])
print(simple_list[2:])
print(simple_list[:-3])

# string is immutable but list is mutable

# list uses references
# above we have to lists (convert_string_to_list, simple_list). Any change in one of the list will reflect in both.
simple_list.append('z')
print('Original List : ', convert_string_to_list)
print('Modified List : ', simple_list)

# There is something called deepcopy() under copy library. It create a new data.
import copy

deep_list = copy.deepcopy(simple_list)
print('Deep List : ', deep_list)
deep_list[2] = 'x'
print('Modified Deep List : ', deep_list)
print('Original List : ', simple_list)