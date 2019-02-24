# importing modules needed for fuctions.
import string
import random

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


def is_valid_level(input):
    valid_level = False
    valid_levels = ["easy", "normal", "hard"]  
    while valid_level is False:
        level = input("Which level would you like to play? ")
        if len(level) >= 1 and level != "" and level.casefold() in valid_levels:
            level = level.casefold()
            return level.casefold()
        elif (SyntaxError, ValueError):
            print("You didn't enter a valid level, please enter: Easy, Normal or Hard.")
        else:
            is_valid_level()

level = is_valid_level(input)

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

word = random_word
print(f"\nThe word has {len(word)} letters in it.\n")
print(word)


def unique_chars(word):
    """Given a string, get all the unique characters."""
    seen_chars = []
    for char in word:
        seen_chars += (char)
    return seen_chars

random_word_string = unique_chars(word)

valid_letters = string.ascii_letters

guess_count = 0
guesses = []
valid_letters = string.ascii_letters
keep_going = False


while keep_going is False:
    pending_word = []
    letter = input("What letter would you like to try?  ")
    if letter not in guesses and letter in valid_letters and guess_count < 7 and letter not in random_word_string and letter != '':
        pending_word = [letter if letter in guesses else "_" for letter in word]
        guesses.append(letter.casefold())
        guess_count += 1
        print(f"\nGuesses available: {8 - guess_count}.\n")
        print(f"These are the letters you have guessed: {guesses}.")
        print([letter if letter in guesses else "_" for letter in word])
    elif letter not in guesses and letter in valid_letters and guess_count < 7 and letter != '':
        pending_word = [letter if letter in guesses else "_" for letter in word]
        guesses.append(letter)
        print(f"\nNice! Try another letter. Guesses available: {8 - guess_count}.\n")
        print(f"These are the letters you have guessed: {guesses}.")
        print([letter if letter in guesses else "_" for letter in word])
    elif letter not in valid_letters or letter == " ":
        print("\nNot a valid guess. Try a different letter.\n")
    elif letter in guesses and letter != '':
        print("\nYou have already tried that letter, try again.\n")
    elif letter is "":
        print("\nNot a valid guess. Try a different letter.\n")
    else:
        keep_going = True
        print([letter if letter in guesses else "_" for letter in word])
        print("\nToo many tries\n")
        print(f"\nThe word was '{word}'.\n")





