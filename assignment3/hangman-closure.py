def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)

        display_word = ""

        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"

        print(display_word)
        
        return all(letter in guesses for letter in secret_word)

    return hangman_closure

secret_word = input("Please enter a secret word: ")

game = make_hangman(secret_word)

won = False

while not won:
    letter = input("Guess a letter: ")
    won = game(letter)


