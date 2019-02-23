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

# level = input("Which level would you like to play? ")
# valid_level = ["easy", "normal", "hard"]
# if level.casefold() in valid_level:
#     print(f"You chose {level}.")
# else:
#     print("Try again!")

def range_level(level):
    level = input("Which level would you like to play? ")
    valid_level = ["easy", "normal", "hard"]
    listOfKeys = []
    if level.casefold() in valid_level and level.casefold() == "easy":
        listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if 4 < value < 6]
        return listOfKeys
    elif level.casefold() in valid_level and level.casefold() == "normal":
        listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if 6 < value < 8]
        return listOfKeys
    elif level.casefold() in valid_level and level.casefold() == "hard":
        listOfKeys = [key  for (key, value) in dict_with_length(unique_words(file)).items() if value > 8]
        return listOfKeys
    else:
        range_level()

random_word = random.choice(range_level(input))
print(f"'{random_word}' is the random word.")