import random

#num = int(input("Enter a number: "))
num = random.randint(3,100000)
print("the starting number is")
print(num)
print("")

while num != 1:
    if (num % 2) == 0:
        num = num // 2
        print(num)
    else:
        num = num * 3 + 1
        print(num)
