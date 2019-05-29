# Write your code here
from random import choice

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

chosen_word = choice(words)
hidden_word = ["-" for letter in chosen_word]
left_tries = 8
uncovered_letters = set()
typed_letters = set()
win = False

while left_tries > 0 and not win:
    print()
    print("".join(hidden_word))

    guess = input("Input a letter: ")

    if len(guess) != 1:
        print("You should print a single letter")
    elif not guess.isascii() or not guess.islower():
        print("It is not an ASCII lowercase letter")
    elif guess in typed_letters:
        print("You already typed this letter")
    elif guess not in chosen_word:
        print("No such letter in the word")
        typed_letters.add(guess)
        left_tries -= 1   
    else:
        uncovered_letters.add(guess)
        typed_letters.add(guess)
        hidden_word = ["-" if letter not in uncovered_letters else letter for letter in chosen_word]
        if uncovered_letters == set(chosen_word):
            win = True
    

if win:
    print("\n" + chosen_word)
    print("You guessed the word!\nYou survived!")
else:
    print("You are hanged!")
