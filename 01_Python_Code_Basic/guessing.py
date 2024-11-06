from  random import randint

print("welcome to our guessing game")

for i in range(1,10):
    guess=int(input("Enter your guess number between 1 to 10:"))
    randomnumber=randint(1,10)

    if guess==randomnumber:
        print("you have win")
        print("The random number was:",randomnumber)

    else:
        print("you have lost")
        print("The random number was:", randomnumber)


