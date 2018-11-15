# dictonary is a (key,value) pair

simple_dict = {'book':1, 'name':'Hello', 'pages':231}
print(simple_dict)

# values are accessed using the keys in the dictonary
print(simple_dict['book'], simple_dict['name'], simple_dict['pages'])

# the order in the dictionary does not matters

# if a key does not exists in the dictionary, it throws a KeyError
try :
    title = simple_dict['title']
except KeyError :
    print('Key does not exists')

# it has same (in, not in) operations as of list
print('Does book exists in dict ', 'book' in simple_dict)
print('Does dict not have title ', 'title' not in simple_dict)

# dictonary has three functions that returns list of key, values and both
# dict.keys() - returns a list of keys
keys = list(simple_dict.keys()) # converts the dict.keys to a list
print('Keys ', keys)

# dict.values() - returns list of values
values = list(simple_dict.values())
print('Values ', values)

# dict.items() - returns list of both keys & values
tuples = list(simple_dict.items())
print('both key & values : ', tuples)

# for loop in dictonary
# for loop on keys
for key in simple_dict.keys() :
    print(key)

# for loop on values
for value in simple_dict.values() :
    print(value)

# for loop on items
for item in simple_dict.items() :
    print(item)

# get(key, (optional)[default value to return if the key is not fount])
print(simple_dict.get('carrey'))

# setdefault(key, value to set if the key is not already set)
simple_dict.setdefault('color', 'brown')
print(simple_dict)
