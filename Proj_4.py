n = 18
Number_of_guesses = 1
print("Number of guesses is limited to only 9 times:")
while (Number_of_guesses <= 9):
    guess_number = int(input("Guess the number:\n"))
    if guess_number <= 15:
        print("You enter the less number, please enter the greater number. \n")
    elif guess_number < 18:
        print("You enter the lesser number but too close to the number, \n")
    elif guess_number > 18 and guess_number <= 23:

        print("You enter greater number but too close too the number, \n")
    elif guess_number >= 23:
        print("You enter the greater number, \n")
    else:
        print("You won the game\n")
        print(Number_of_guesses, "No. of guesses he took to complete the game")
        break
    print(9-Number_of_guesses, "No.of guesses left")
    Number_of_guesses = Number_of_guesses + 1

    if(Number_of_guesses>9):
        print("Game over, better luck next time")
        break



