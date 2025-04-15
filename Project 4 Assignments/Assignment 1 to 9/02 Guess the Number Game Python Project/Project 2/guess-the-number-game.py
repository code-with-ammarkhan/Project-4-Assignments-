import random

def guess_the_number_computer():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Computer ne 1 se 100 ke darmiyan ek number socha hai. Guess karo!")

    while guess != number:
        guess = int(input("Apna guess do: "))
        attempts += 1

        if guess < number:
            print("Zyada bara number guess karo.")
        elif guess > number:
            print("Zyada chhota number guess karo.")
        else:
            print(f"Shabash! Tumne {attempts} tries mein sahi guess kiya.")

guess_the_number_computer()
