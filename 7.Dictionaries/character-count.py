message = 'i am watching mission impossible three. tom cruise is the actor'
count = {}

for char in message :
    if count.get(char, 0) == 0 :
        count.setdefault(char, 1)
    else :
        count[char] = count[char] + 1

print("Using Java Logic : ", count) 

count2 = {}
for char in message :
    count2.setdefault(char, 0)
    count2[char] = count2[char] + 1

print("Python logic : ",count2)

import pprint
# pprint() - pretty prints a dictonary
pprint.pprint( count2)
    

