# 1) list of words = "words.txt"
#     - read file
#     - create dictionary
#     - create value of length per key
#     - add value for length per key in dictionary
# 2) Create Levels
#     - Easy is key.value(length) = length > 4 and length < 6
#     - Normal is key.value(length) = length > 6 and length < 8
#     - Hard is key.value(length) = length > 8
#     - Based on these levels add level value to dictionary for words
#     - add level to dictionary
# 3) Message saying, "Welcome to Mystery Word! My name is Jarvis and I will be selecting a random word for you to guess. You will have a total of 8 guesses. If you do not guess within 8 guesses, the round will be over and you have a chance to try another random word, or quit the game. Now that we are ready to start, I need you to pick the level. Easy, Normal or Hard. Which level would you like to play?"
# 4) User enters the level.
#     - The game will need to store the level during the following steps at the beginning of each round
#     - it will need to return the level for the next function
# 5) Based on level selected the system can then filter keys with values of level.
#     - will need to return new list for random picker
# 6) based on that list or random word, the function random_word can run. 
#     - will need to return random word with 
#         - value of length and print ("Your word is {x} letters long!")
#         - then an input(prompt("Please enter a single letter to see if it is in the word."))
#         - the value will need to be used in the validate letter function
#             - based on the word, a new list of valid characters will need to be returned for the next function
# 7) The system will then need to complete a total of 8 loops (while condition)
#     - need to store total of guesses = 8 with a start of 0 that increments by 1 for each "qualified-guess"
#         - qualified guess will need an ongoing list of "guessed_letters"
#         - need a list of "letters_not_guessed"
#         - if the letter == valid_characters, update letter in index from "_" to "letter" and return "guessing_state_word"
#         - qualified guess is a letter that is not "true" and has not already been guessed (letter != guessed_letter_list)
#     - qualifiers
#         - only 1 letter. 
#             - if more then say ("Too many letters! Try again, but only one this time.")
#         - no punctuations or numbers, if entered print ("Can only enter 1 letter. Try again.")
#             - both will need to go back to qualify-guess. 
# 8) if user gets to 8 round with any "incomplete_letters", the system then says "The round is over! The word you needed to guess is {random_word}! Great try though!? 
#     - input(prompt("would you like to try again? ")
#         if user says "yes" then start over at the top of the program.prompt
#         if user says "no" then quit the program and print ("Thanks for playing!")
# 9) other needs
#     - no PEP8 warning or errors


import string, random

print("""Welcome to Mystery Word! My name is Jarvis and I will be selecting a random word for you to guess. You will have a total of 8 guesses. If you do not guess within 8 guesses, the round will be over and you have a chance to try another random word, or quit the game. Now that we are ready to start, I need you to pick the level. Easy, Normal or Hard.""")

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

# dictOfWords = dict.fromkeys(unique_words(file) , 0)

def dict_with_length(words):
    """take list of words and count characters"""
    word_length = {}
    for word in words:
        if word in word_length:
            word_length[word] = word_length[word] + len(word)
        else:
            word_length[word] = len(word)
    
    return word_length

new_dictionary = dict_with_length(unique_words(file))

level = input("Which level would you like to play? ")
valid_level = ["easy", "normal", "hard"]
# age = int(age_as_a_string)
if level in valid_level:
    print(f"You chose {level}.")
else:
    print("Try again!")


        

# pulls list of words from dictionary that have values
# listOfKeys = [key  for (key, value) in new_dictionary.items() if value == 9]
listOfKeys = [key  for (key, value) in new_dictionary.items() if 4 < value < 6]

random_word = random.choice(listOfKeys)
print(random_word)
print(level)

word = random_word

guesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
[letter if letter in guesses else "_" for letter in word]

current_guesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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




# print(f"Your word is {listOfKeys} letters." )
# print(dict_with_length(unique_words(file))
# print(new_dictionary.items())
# print(level.lower())
# pulls list of keys
# print(list(dictOfWords.values()), )





