# List compreheshions is not required to be used by general but we can use this 
# to make easy calculations


prizes = [1,2,3,4,5,6,7,8]

dbl_prizes =[]

# double the prizes will be

# using for loop
for prize in prizes:
    dbl_prizes.append( prize * 2)

print(dbl_prizes)

# using list compreheshions
dbl_prizes1 = [prize * 2 for prize in prizes ]
print(dbl_prizes1)


# Squared of even numbers
Squared = [1,2,3,4,5,6,7,8]

Squared_evn = [ Square**2  for Square in Squared if (Square ** 2)%2==0]
print(Squared_evn)