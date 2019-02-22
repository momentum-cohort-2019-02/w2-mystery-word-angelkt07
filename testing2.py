random_word = str("scuse")

word = random_word

def unique_chars(word):
    """Given a string, get all the unique characters."""
    seen_chars = []
    for char in word:
        seen_chars += (char)
    return seen_chars

print(f"This is the word in an a new string to guess against: {unique_chars(word)}")

index_to_match = unique_chars(word)

print(f"this is your index to match: {index_to_match}")

valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                   "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

keep_going = False
letter = str(input("What letter would you like to use? "))
if letter not in valid_letters:
    print("Try again, and only enter 1 letter!")
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





