import sys
import os
import time
import random


def quit():
    print("Quitting the game now...")
    if sys.platform.startswith('win'):
        # For Windows
        SystemExit or os._exit(0) or sys.exit()
    else:
        # For Linux, macOS, and other Unix-like systems
        SystemExit or os._exit(0) or sys.exit()
    

def play_again(): # Function to ask the user if they want to play again
   answer = input("Would you like to play again? Enter yes or no: ").lower()
   if answer == "yes":
      game()
   elif answer == "no":
      print("Thanks for playing! Goodbye!")
      time.sleep(2)
      restart_game()    
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
            print("I will give you another chance, please enter a number between 1 and 10.")
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

def restart_game(): # Main Menu          
    print("if you want to play again type yes")
    print("If you would like to quit, type no")
    answer = input("Enter yes or no: ").lower()
    if answer == "yes":
        user_name = input("Enter your name: ")
        print(f"Welcome {user_name}!")
        game()
    elif answer == "no":
        print("Sweet as, shutting it down in 1...2...pft")
        time.sleep(2)
        quit()
    else:
        print("Invalid input, please enter yes or no in lowercase.")
        main_menu()

def main_menu(): # Main Menu          
    print("Would you like to play?")
    answer = input("Enter yes or no: ").lower()
    if answer == "yes":
        user_name = input("Enter your name: ")
        print(f"Welcome {user_name}!")
        game()
    elif answer == "no":
        print("Okay, maybe next time!")
        restart_game()
    else:
        print("Invalid input, please enter yes or no in lowercase.")
        main_menu()

print("Hello this is a numbers guessing game!")
main_menu()
