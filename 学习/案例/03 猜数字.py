import random

random_num = random.randint(1, 101)
print(random_num)
while True:
    inp = int(input("num:"))
    if inp == random_num:
        print("猜对了!")
        break
    elif inp > random_num:
        print("大了")
    elif inp < random_num:
        print("小了")


