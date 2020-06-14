#radhe radhe
# write a python program which will keep adding
# a stream of numbers inputed by user


sum = 0
list = []
while True:
    q = "q"
    userInput = input("Enter the item price: \n")
    if userInput != 'q':
        list.append(userInput)
        sum = sum + int(userInput)
        print(f"Your order so far is: {sum}")

    else:
        print(f"Your Total Order Is {sum}. Keep visiting us.")
        break
    

print("\n")
cnt = 0
print("Sri Ram Kirana General Store")
print("Your item are: ")
for i in list:
    cnt = cnt + 1
    print(f"{cnt}."+list[cnt-1])