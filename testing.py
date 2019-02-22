word = str("scuse")

def unique_chars(word):
    """Given a string, get all the unique characters."""
    seen_chars = []
    for char in word:
        seen_chars += (char)
    return seen_chars

random_word_string = unique_chars(word)
guesses = ["G", "E", "T"]

[letter if letter in guesses else "_" 
for letter in random_word_string]

print(unique_chars(word))
print(random_word_string)
print(word)
