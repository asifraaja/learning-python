# A simple if, else if & else statement
# checking if the username and password are valid.

print('Enter username :')
username = input()
print('Enter password :')
password = input()

if username == 'm0a00pf' and password == 'password' :
    print('successfull login')
elif username == 'm0a00pf' :
    print('Password is wrong')
else:
    print('Username & password is wrong')

# Note:
### a blank string is a false statement
# a non-blank string is a true statement
# 0 is a false statement
# everything is else than 0 is a true statement
# bool(data) - function returns the boolean value of the data
#  
