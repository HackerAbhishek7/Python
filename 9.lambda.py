# tutorial to show lambda function
# The power of lambda is better 
# shown when you use them as 
# an anonymous function inside 
# another function.

# Syntax : lambda Arguments : Expression

# x = lambda a, b: a + b
# print(x(4,5))


def munum(n):
    return lambda a: a * n

mydoubler = munum(5)

print(mydoubler(12))
