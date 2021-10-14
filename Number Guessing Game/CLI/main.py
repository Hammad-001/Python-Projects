import random

def start_game():
    number_of_guesses = 4
    number = int(random.random()*100)
    while number_of_guesses > 0:
        try:
            guess = int(input("Enter guess: "))
            if guess == number:
                print("You Won!")
                break
            elif abs(guess-number) > 20:
                number_of_guesses -= 1
                print("Guess is Far from the Number! Guess Remaining:", str(number_of_guesses))
            else:
                number_of_guesses -= 1
                print("Guess is Close to the Number! Guess Remaining:", (number_of_guesses))
        except Exception:
            print("Invalid guess!!!")

        finally:
            if number_of_guesses == 0:
                print("You Lose!!!")

START = input("Enter Y/N: ")

if START == "Y" or START == "y":
    start_game()