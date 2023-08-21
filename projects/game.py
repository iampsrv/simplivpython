import random

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    
    max_attempts = int(input("How many attempts would you like? "))
    attempts = 0

    for attempts in range(1, max_attempts + 1):
    #while attempts < max_attempts:
        guess = int(input("Take a guess: "))
        attempts += 1 # attempts = attempts
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts+1} attempts!")
            #return
            break
    
    print(f"Sorry, you ran out of attempts! The secret number was {secret_number}. Better luck next time!")
    
play_guessing_game()
