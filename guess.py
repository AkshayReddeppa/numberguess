import random
number =random.randint(0,100)
print(number)
for x in range(3):
    guess = int(input("enter the number you guess ?"))
    if guess == number :
        print("you guessed right !! WON ")
        break
    else:
        diff = number -guess
        if diff < 3 and  diff > -3:
            print("too low")
        else:
            print("too high")
        continue
