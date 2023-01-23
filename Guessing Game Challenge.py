import random
num=random.randint(1,100)

print("Welcome to Guessing Game Challenge")
print("I am thnking of a number from 1 to 100")
print("If your guess more than 10 away from number, i will say You are COLD")
print("If your guess is within 10 of my number, I will you are WARM")
print("If your guess is father than your recent guess, I will say you are  COLDER")
print(" If your guess is closer than your previous guess, I will say you are WARMER ")
print ("LETS PLAY")


guesses=[0]

while True:
    guess=int(input("I am thnking of a number from 1 to 100.\n What is your guess?"))
    if guess < 1 or guess > 100:
         print("OUT OF BONDS!, PLEASE TRY AGAIN")
         continue
    if guesses==num:
         print("CONGRATULATIONS,YOU GUESSED IT IN ONLY {len(guesses} ")
         Break

    guesses.append(guess)
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("WARMER!")
        else:
            print("COLDER!")

    else:
        if abs(num-guess) <=10:
            print("WARM")
        else:
            print("COLD")








