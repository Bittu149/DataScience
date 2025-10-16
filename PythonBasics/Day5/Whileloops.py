#While loop
# a = int(input("Enter your number :- "))
# while a > 0:
#     print(a%10)
#     a = a//10

# a = int(input("Enter your number :- "))
# rev = 0
# while a > 0:
#     rev = rev*10 + a % 10
#     a = a//10

# print(rev)

##Guessing number game
import random
num = random.randint(1,11)
tries = 0
while True:
    print(num)
    guess = int(input("Please guess your number between 1 and 11 :- "))

    if num == guess:
        tries+=1
        print(f"You are right you guessed the number is {tries} tries ")
        break

    elif num <guess:
        print("Go a little lower")
        tries+=1

    elif num> guess:
        print("Go a little higher ")
        tries+=1

    else:
        tries +=1
        print("Sorry you are wrong")



