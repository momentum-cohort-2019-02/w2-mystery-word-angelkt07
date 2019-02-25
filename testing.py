
def is_valid_answer(input):
    play_again_input = False
    correct_answers = ["yes", "no"] 
    while play_again_input is False:
        play_again = input("Would you like to play again? Yes or No  ")
        if play_again in correct_answers and play_again.casefold() == "no":
            play_again_input = False
        elif (SyntaxError):
            print("You didn't enter a valid answer, please enter a answer.")
        else:
            valid_answer()