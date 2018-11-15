for i in [0,1,2,3]:
    print(i)

print(list(range(5)))
print(list(range(0,10, 3)))
print(list(range(10, -10, -2)))

supplies = ['pens', 'notebooks', 'binders']
for i in range(len(supplies)):
    print(supplies[i])


# Multiple Assignment 
# Assign the list values to the left-hand-side variables in one shot instead of having to reassgin it multiple times.
cat = ['animal', 'four-legged', 'yes']
creature, no_of_legs, bites = cat
print(creature, no_of_legs, bites)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size, color, disposition)

# Most useful trick with multiple assignments is swapping 
# Normal Swapping
a = 10
b = 20
print('Initial Values a : ',a,' b : ',b)
temp = a
a = b
b = temp
print('a : ',a,' b : ',b)

#Multiple Assignment Swap
a = 10
b = 20
a, b = b, a
print('a : ',a,' b : ',b)