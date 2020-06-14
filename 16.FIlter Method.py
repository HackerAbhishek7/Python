# A simple tutorial to show the filter 
# methods in python

grades = ['A','B','C','F']

def remove_fails(grades):
    return grades!='F'

# print(list(filter(remove_fails,grades)))
filter_grades = []

for grade in grades:
    if grade != 'F':
        filter_grades.append(grade)

print(filter_grades)

# List comprehensions
filter_grades1 = [grade for grade in grades if grade!='F']
print(filter_grades1)