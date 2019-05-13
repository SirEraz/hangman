from random_word import RandomWords
r = RandomWords()
spacer = str("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
space = str(" ")

def hangmanSingleplayer():
    maxChar = str(input("What should the maximum amount of letters be?\n"))
    word = r.get_random_word(hasDictionaryDef="true", maxLength=maxChar)
    chars = list(word)
    length = len(word)
    print(chars)
    blanks = []
    for i in range(length):
        blanks.append("_ ")
    gameactive = True
    hangman_head = str("    |")
    hangman_arms_body = str("    |")
    hangman_legs = str("    |")
    guessed = []
    correctLetters = int(0)
    wrongLetters = int(0)
    while gameactive == True:
        print("Word is {} letters long.".format(length))
        blankstr = "".join(blanks)
        print(blankstr)
        print("    _________")
        print("    |         |")
        print(hangman_head)
        print(hangman_arms_body)
        print(hangman_legs)
        print("    |\n    |")
        guessedStr = "".join(guessed)
        print("You've guessed: {}".format(guessedStr))
        guess = str(input("Guess a letter: "))
        guessed.append("{} ".format(guess))
        if guess in chars:
            print("'{}' is in the word!".format(guess))
            for i, j in enumerate(chars):
                if j == guess:
                    newLetter = guess + space
                    blanks[i] = newLetter
                    correctLetters = correctLetters + 1
        else:
            print("'{}' is not in the word!".format(guess))
            wrongLetters = wrongLetters + 1
            print(spacer)
        if correctLetters == len(word):
            print(spacer)
            print("You win! You guessed the word: {}".format(word))
            gameactive = False
            print(spacer)
        elif wrongLetters == 1:
            hangman_head = str("    |         0")
        elif wrongLetters == 2:
            hangman_arms_body = str("    |        /")
        elif wrongLetters == 3:
            hangman_arms_body = str("    |        /|")
        elif wrongLetters == 4:
            hangman_arms_body = str("    |        /|\ ")
        elif wrongLetters == 5:
            hangman_legs = str("    |        /")
        elif wrongLetters == 6:
            hangman_legs = str("    |        / \ ")
            print("    _________")
            print("    |         |")
            print(hangman_head)
            print(hangman_arms_body)
            print(hangman_legs)
            print("    |\n    |")
            print("You lost! The correct word was {}".format(word))
            gameactive = False
            print(spacer)
def hangmanMultiplayer():
    print(spacer)
    word = str(input("Enter the secret word: "))
    chars = list(word)
    length = len(word)
    print(chars)
    print(spacer)
    blanks = []
    for i in range(length):
        blanks.append("_ ")
    gameactive = True
    hangman_head = str("    |")
    hangman_arms_body = str("    |")
    hangman_legs = str("    |")
    guessed = []
    correctLetters = int(0)
    wrongLetters = int(0)
    while gameactive == True:
        print("Word is {} letters long.".format(length))
        blankstr = "".join(blanks)
        print(blankstr)
        print("    _________")
        print("    |         |")
        print(hangman_head)
        print(hangman_arms_body)
        print(hangman_legs)
        print("    |\n    |")
        guessedStr = "".join(guessed)
        print("You've guessed: {}".format(guessedStr))
        guess = str(input("Guess a letter: "))
        guessed.append("{} ".format(guess))
        if guess in chars:
            print("'{}' is in the word!".format(guess))
            enter = str(input("Press enter to continue."))
            for i, j in enumerate(chars):
                if j == guess:
                    newLetter = guess + space
                    blanks[i] = newLetter
                    correctLetters = correctLetters + 1
            print(spacer)
        else:
            print("'{}' is not in the word!".format(guess))
            enter = str(input("Press enter to continue."))
            wrongLetters = wrongLetters + 1
            print(spacer)
        if correctLetters == len(word):
            print(spacer)
            print("You win! You guessed the word: {}".format(word))
            enter = str(input("Press enter to return to menu."))
            gameactive = False
            print(spacer)
        elif wrongLetters == 1:
            hangman_head = str("    |         0")
        elif wrongLetters == 2:
            hangman_arms_body = str("    |        /")
        elif wrongLetters == 3:
            hangman_arms_body = str("    |        /|")
        elif wrongLetters == 4:
            hangman_arms_body = str("    |        /|\ ")
        elif wrongLetters == 5:
            hangman_legs = str("    |        /")
        elif wrongLetters == 6:
            hangman_legs = str("    |        / \ ")
            print(spacer)
            print("    _________")
            print("    |         |")
            print(hangman_head)
            print(hangman_arms_body)
            print(hangman_legs)
            print("    |\n    |")
            print("You lost! The correct word was {}".format(word))
            enter = str(input("Press enter to return to menu."))
            gameactive = False
            print(spacer)
while True:
    print("HANGMAN")
    print("1 - Start Game\n2 - Exit")
    menu = int(input("Enter: "))
    if menu == 2:
        exit()
    elif menu == 1:
        print(spacer)
        print("Play Options:\n")
        print("1 - Play alone\n2 - Play together")
        submenu = int(input("Enter: "))
        if submenu == 1:
            hangmanSingleplayer()
        elif submenu == 2:
            hangmanMultiplayer()
        else:
            print("Unknown input.")
            print("Press enter to return to menu.")
            PE = str(input(""))
            print(spacer)
    else:
        print("Unknown input.")
        print("Press enter to return to menu.")
        PE = str(input(""))
        print(spacer)
