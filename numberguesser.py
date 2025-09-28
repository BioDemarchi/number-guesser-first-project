
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
   guessed_number = int(random.randint(1, 10)) # Random number between 1 and 10
   attempts = 3 # Number of attempts for each game
   print("I have selected a number between 1 and 10. You have 3 attempts to guess it.")
   number_guessed = int(input("Enter your guess: "))
   if type(number_guessed) != int:
       print("Invalid Input, please enter a number!")
       game()
   while attempts > 0:
         if number_guessed > 10 or number_guessed < 1:
            print("Please enter a number between 1 and 10.")
            number_guessed = int(input("Enter your guess: "))
         elif number_guessed == guessed_number:
              print("congratulations! You guessed the number right!")
              play_again()
         elif number_guessed != guessed_number:
            attempts -= 1 # Decrease attempts by 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if number_guessed != guessed_number and attempts == 1:
                print("This is your last attempt, make it count!")
                print("Hint: the number is " + ("even" if guessed_number % 2 == 0 else "odd") + ".")
            if attempts == 0:
                print(f"Sorry, you've used all your attempts. The correct number was {guessed_number}.")
                play_again() 
            if number_guessed == str:
                print("Invalid Input, please enter a number!")
            else:
                print("Invalid number, use a number between 1 and 10.") 
                attempts + 1

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


print("Hello this is a guessing game!")
main_menu()