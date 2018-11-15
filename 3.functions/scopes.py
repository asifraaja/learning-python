### Learning about the scope of variable
# There are two scopes i.e., Local & Global
# variables specified inside a block of code i.e., function, loop, conditional are considered to be local scope
# Example of a local scope
def myFunction() :
    a = 2   # This variable is in a local scope. The variable is cannot be used outside the block
    b = 3
    print( a , b )