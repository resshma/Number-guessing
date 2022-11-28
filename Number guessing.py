import random

top = input("Enter a number: ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print('Enter a number greater than 0')
        quit()

else:
    print('Enter a number')
    quit()

random_number = random.randint(0, top )
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
       if user_guess = int(user_guess)
    else:
        print("Enter a number next time: ")
        continue
    
    if user_guess == random_number:
        print("Correct! ")
        break
    elif user_guess > random_number:
        print("You are above the number! ")
    else:
        print("You are below the number! ")

print("That's right. You got it in", guess, "guess")
