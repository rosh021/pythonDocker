from random import randint

min_number = int(input("Please Enter the min number: "))
max_number = int(input("please Enter the max number: "))

if(max_number < min_number):
    print("invalid input - shutting down ...")

else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)