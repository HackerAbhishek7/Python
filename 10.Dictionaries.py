# A tutorial to show dictionarary in python

# ninja_belts = {'ruy':'red', 'Hattori':'Black'}
# print(ninja_belts)

# print('yoshoi' in ninja_belts)

# vals = list(ninja_belts.values())
# print(vals)


def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print("i am "+ key +" and i am "+ val)

ninja_belts = {}
while True:
    ninja_name = input('Enter ninja name :')
    ninja_value = input('Enter ninja values :')

    ninja_belts[ninja_name] = ninja_value

    out = input('Do you want to add more (y/n)')
    if out == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)