# A password must be strong
import string
import random


s = []

if __name__ == "__main__":

    # take strings

    s1 = string.ascii_lowercase
    # print(s1)

    s2 = string.ascii_uppercase
    # print(s2)

    s4 = string.digits
    # print(s4)

    s3 = string.punctuation
    # print(s3)

    # input password length
    plen = int(input("Enter Password Length: \n"))
    
    # extend it into a empty list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    #    then suffle
    random.shuffle(s)
    print("Your Password Is: ")
    print("".join(s[0:plen]))






