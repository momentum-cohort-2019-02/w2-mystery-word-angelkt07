#importing modules needed for fuctions.
import string, random

print("""Welcome to Mystery Word!\nMy name is Jarvis and I will be selecting a random word for you to guess.\nYou will have a total of 8 guesses.\nIf you do not guess within 8 guesses, the round will be over and you have a chance to try another random word, or quit the game.\nNow that we are ready to start, I need you to pick the level: Easy, Normal or Hard.""")

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

file = "words.txt"

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

#creates dictionary with length
def dict_with_length(words):
    """take list of words and count characters"""
    word_length = {}
    for word in words:
        if word in word_length:
            word_length[word] = word_length[word] + len(word)
        else:
            word_length[word] = len(word)
    
    return word_length

def range_level(level):
    level = input("Which level would you like to play? ")
    valid_level = ["easy", "normal", "hard"]
    listOfKeys = []
    if level.casefold() in valid_level and level.casefold() == "easy":
        listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if 4 <= value <= 6]
        return listOfKeys
    elif level.casefold() in valid_level and level.casefold() == "normal":
        listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if 6 <= value <= 8]
        return listOfKeys
    elif level.casefold() in valid_level and level.casefold() == "hard":
        listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if value >= 8]
        return listOfKeys
    else:
        range_level()

random_word = random.choice(range_level(input))
print(f"'{random_word}' is the random word.")

word = random_word

# def unique_chars(word):
#     """Given a string, get all the unique characters."""
#     seen_chars = []
#     for char in word:
#         seen_chars += (char)
#     return seen_chars

# random_word_string = unique_chars(word)

# print(f"The word is {len(word)} characters long.")

# print(f"this is your index to match: {random_word_string}")

valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                   "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letter = str(input("What letter would you like to use? "))
if letter not in valid_letters:
    print("Try again, and enter 1 letter!")
else:
    letter = letter.casefold()

print(f"You picked letter {letter}!")
print("Let's see if this matches any letter in the word.")

guesses = letter

print([letter if letter in guesses else "_" for letter in word])

new_word = [letter if letter in guesses else "_" for letter in word]

current_guesses = letter

def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

print([display_letter(letter, current_guesses) for letter in word])

total_limit = 8

print(f"You have a total of {total_limit} times to guess.")







