word = "MAGNITUDE"
guesses = ["G", "E", "T"]

[letter if letter in guesses else "_" 
 for letter in word]

current_guesses = ["G", "E", "T"]

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