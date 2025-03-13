import random
n = random.randint(1, 100)

a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess the number: "))
    if(a >n):
        print("Lower number plese")
    else:
        print("higher number please") 
        guesses +=1

print(f"You have guessed the number {n} coorectly in {guesses} attempt")   
