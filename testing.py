def is_valid_letter(input):
    valid_letter = False
    valid_letters = string.ascii_letters.casefold() 
    letter = input("What letter would you like to try?  ")
    while valid_letter is False:
        if len(letter) is 1 and letter != "" and letter.casefold() in valid_letters:
            letter = letter.casefold()
            return letter
        elif (SyntaxError, ValueError):
            print("You didn't enter a valid letter, please enter a letter.")
        else:
            is_valid_letter()