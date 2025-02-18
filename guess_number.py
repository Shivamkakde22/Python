# Write a program that allows the user to guess a randomly generated number within 
# a certain number of attempts using a while loop
import random
def guess_number():
    number_guess = random.randint(1,10)
    attempt = 0
    max_attempt = 10

    print("Welcome to guessing number game!!")
    print("Try to Guess number 1 to 10")

    while attempt<max_attempt:
        guess = int(input("Enter the Number: "))
        attempt+=1

        if guess<number_guess:
            print("You are running too low!!")
        elif guess>number_guess:
            print("Your Guess number is too high")
        else:
            print("Congratulation You guess the correct number")
        
        print("Correct Number is",number_guess)
        
    if guess!=guess_number:
        print("Your are out off attempt!!")

print(guess_number())