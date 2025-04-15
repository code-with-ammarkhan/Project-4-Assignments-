import random

def get_word():
    words = ["python", "developer", "hangman", "streamlit", "project", "variable", "function", "loop", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = get_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman (Medium Version)!")
    print("You have", attempts, "attempts to guess the word.")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        elif guess not in word:
            attempts -= 1
            print("Wrong guess. Attempts left:", attempts)
        else:
            print("Good job!")

        guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nOut of attempts. The word was:", word)

hangman()
