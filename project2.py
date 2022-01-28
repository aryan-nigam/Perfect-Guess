import random
randnumber=random.randint(1,100)
guesses=0
userguess=None
while(userguess!=randnumber):
 userguess=int(input("enter your guess: "))
 guesses+=1
 if(userguess==randnumber):
    print("you guessed it right")
 else:
    if(userguess>randnumber):
     print("you guesses it wrong!enter a smaller number")    
    else:
     print("you guessed it wrong!please enter a higher number")

print(f"you guessed the number in {guesses} guesses")