
import os
import time
import random


def clear_console(): # Function to clear the console
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')

def play_again(): # Function to ask the user if they want to play again
   answer = input("Would you like to play again? Enter yes or no: ").lower()
   if answer == "yes":
      game()
   elif answer == "no":
      print("Thanks for playing! Goodbye!")
      print("Console will clear in two seconds.")
      time.sleep(2)
      clear_console()
      quit()    
   else:
      print("Invalid input, please enter yes or no in lowercase.")
      play_again()

def game(): # Main Game Logic
   correct = int(random.randint(1, 10)) # Random number between 1 and 10
   attempts = 3 # Number of attempts for each game
   print("I have selected a number between 1 and 10. You have 3 attempts to guess it.")
   while True: # Loop until the game ends
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 10.")
            continue

        if guess < 1 or guess > 10:
            print("I will give you another chance, please use a number between 1 and 10")
            continue

        if guess == correct:
            print("Congratulations! You guessed the correct number!")
            play_again()
            break
        else:
            attempts -= 1
            if attempts == 0:
                print(f"Sorry, you've run out of attempts. The correct number was {correct}.")
                play_again()
                break
            elif attempts == 1:
                print("This is your last attempt, make it count!")
                print("Hint: the number is " + ("even" if correct % 2 == 0 else "odd") + ".")
            else:
                print(f"Wrong number! You have {attempts} attempts left.")

def main_menu(): # Main Menu          
    print("Would you like to play?")
    answer = input("Enter yes or no: ").lower()
    if answer == "yes":
        user_name = input("Enter your name: ")
        print(f"Welcome {user_name}!")
        game()
    elif answer == "no":
        print("Okay, maybe next time!")
        print("Console will clear in two seconds.")
        time.sleep(2)
        clear_console()
    else:
        print("Invalid input, please enter yes or no in lowercase.")
        main_menu()


print("Hello this is a numbers guessing game!")
main_menu()