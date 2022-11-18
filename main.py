import random
randNumber = random.randint(1,99)
yourGuess = None
guesses = 0
while(yourGuess != randNumber):
  yourGuess = int(input("Enter the two digit number of your guess:  "))
  guesses  += 1
  if(yourGuess ==randNumber):
    print("You guessed it right!")
  else:
        if(yourGuess>randNumber):
         print("You guessed it wrong! Enter a smaller number")
        else:
              print("You guessed it wrong! Enter a larger number")
    
print(f"You guessed the number in {guesses} guesses")
with open("highscore.txt", "r") as f:
  highscore = int(f.read())

if(guesses<highscore): 
  print("Congratulations! you just achieved a highscore")
  with open("highscore.txt", "w") as f:

   f.write('%d' %guesses)