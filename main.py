import random
randNumber = random.randint(0,9)
print(randNumber)

yourGuess = int(input("Enter the number of your guess:  "))
if(yourGuess ==randNumber):
    print("You guessed it right!")
else:
    print("you")
