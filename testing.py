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
        listOfKeys = "easy"
        return listOfKeys
    elif level == "normal":
        listOfKeys = "normal"
        return listOfKeys
    else:
        listOfKeys = "hard"
        return listOfKeys

print(range_level(level))