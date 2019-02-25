# importing modules needed for fuctions.
import string
import random

# TELL THE USER HOW TO PLAY THE GAME.
print("""\nWelcome to Mystery Word!\n\nMy name is Jarvis and I will be selecting a random word for you to guess.\nYou will have a total of 8 guesses.\nIf you do not guess within 8 guesses, the round will be over and you have a chance to try another random word, or quit the game.\nNow that we are ready to start, I need you to pick the level: Easy, Normal or Hard.\n""")

# assigned file as a variable
file = "words.txt"

# Takes a list from a file and removes bad characters
def new_list_words(text_file):
    """take a file, get unique words, turn them into all lowercase, no puncs, replace all whitespace with 1space. """

    text_file = text_file.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits

    # remove punc
    new_text = ""
    for char in text_file:
        if char in valid_chars:
            new_text += char

    text_file = new_text
    text_file = text_file.replace("\n", " ")
    return text_file

# creates list of strings of words:
def unique_words(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file) as file:
        text_file = file.read()

    text_file = new_list_words(text_file)
    words = []
    for word in text_file.split(" "):
        if word != '':
            words.append(word)

    return words

# creates dictionary with length
def dict_with_length(words):
    """take list of words and count characters"""
    word_length = {}
    for word in words:
        if word in word_length:
            word_length[word] = word_length[word] + len(word)
        else:
            word_length[word] = len(word)
    return word_length

game_over = False

# Game round so the user can play over and over if they wanted.
while game_over is False:
    if game_over is False:
        # validates the answer from the user in case they just hit enter or incorrect answer
        def is_valid_level(input):
            """Is the level the user entered valid"""

            valid_level = False
            valid_levels = ["easy", "normal", "hard"]  

            # https://stackoverflow.com/questions/26247729/how-do-i-get-python-to-recognize-that-there-has-been-no-input for the SyntaxError & ValueError
            while valid_level is False:
                level = input("Which level would you like to play? ")
                if len(level) >= 1 and level != "" and level.casefold() in valid_levels:
                    level = level.casefold()
                    return level.casefold()
                elif (SyntaxError):
                    print("You didn't enter a valid level, please enter: Easy, Normal or Hard.")
                else:
                    is_valid_level()

        level = is_valid_level(input)

        # takes the level and says pick a random key from the dictionary where the length matches the requirements.
        def range_level(level):  
            listOfKeys = []
            if level == "easy":
                listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if 4 <= value <= 6]
                return listOfKeys
            elif level == "normal":
                listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if 6 <= value <= 8]
                return listOfKeys
            else:
                listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if value >= 8]
                return listOfKeys

        random_word = random.choice(range_level(level))
        # print(f"'{random_word}' is the random word.")
        print(f"\nThe word has {len(random_word)} letters in it.\n")
        #   


        def unique_chars(random_word):
            """Given a string, get all the unique characters."""
            seen_chars = []
            for char in random_word:
                seen_chars += (char)
            return seen_chars

        random_word_string = unique_chars(random_word)

        valid_letters = string.ascii_letters

        pending_word = []
        keep_going = False
        guesses = []
        guess_count = 0

        while keep_going is False:
            # is the letter valid
            def is_valid_letter(input):
                valid_letter = False
                valid_letters = string.ascii_letters.casefold() 
                while valid_letter is False:
                    letter = input("What letter would you like to try?  ")
                    if len(letter) is 1 and letter != "" and letter.casefold() in valid_letters:
                        letter = letter.casefold()
                        return letter
                    elif (SyntaxError):
                        print("You didn't enter a valid letter, please enter a letter.")
                    else:
                        is_valid_letter()

            letter = is_valid_letter(input)

            # takes the letter and compares: in guess list? meets guess count? in random_word?
            if letter.casefold() not in guesses and guess_count < 7 and letter.casefold() not in random_word_string:
                pending_word = [letter if letter.casefold() in guesses else "_" for letter in random_word]
                guesses.append(letter.casefold())
                guess_count += 1
                print(f"Guesses available: {8 - guess_count}.")
                print(f"These are the letters you have guessed: {guesses}.")
                print(f"{[letter if letter.casefold() in guesses else '_' for letter in random_word]}\n")
            elif letter.casefold() not in guesses and letter.casefold() in random_word_string and guess_count < 7:
                guesses.append(letter.casefold())
                if [letter if letter.casefold() in guesses else "_" for letter in random_word] == random_word_string:
                    keep_going = True
                    print([letter if letter.casefold() in guesses else "_" for letter in random_word])
                    print("You win")
                    play_again = input("Would you like to play again? Yes or No  ")
                    if play_again.casefold() == "no":
                        game_over = True
                    else:
                        game_over = False
                else: 
                    print(f"Nice! Try another letter. Guesses available: {8 - guess_count}.")
                    print(f"These are the letters you have guessed: {guesses}.")
                    print(f"{[letter if letter.casefold() in guesses else '_' for letter in random_word]}\n")
                pending_word = [letter if letter.casefold() in guesses else "_" for letter in random_word]
                guess_count += 0
            elif letter in guesses:
                print("You have already tried that letter, try again.\n")
            else:
                keep_going = True
                print([letter if letter.casefold() in guesses else "_" for letter in random_word])
                print("\nToo many tries\n")
                print(f"The word was '{random_word}'.")
                play_again = input("Would you like to play again? Yes or No  ")
                if play_again.casefold() == "no":
                    game_over = True
                else:
                    game_over = False


        





