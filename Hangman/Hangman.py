# Write your code here
from random import choice

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

chosen_word = choice(words)
hidden_word = ["-" for letter in chosen_word]
left_tries = 8
uncovered_letters = set()

while left_tries > 0:
    print()
    print("".join(hidden_word))

    guess = input("Input a letter: ")

    if guess not in chosen_word:
        print("No such letter in the word")
        left_tries -= 1
    elif guess in uncovered_letters:
        print("No improvements")
        left_tries -= 1
    else:
        uncovered_letters.add(guess)
        hidden_word = ["-" if letter not in uncovered_letters else letter for letter in chosen_word]
        if uncovered_letters == set(chosen_word):
            print("\n" + chosen_word)
            print("You guessed the word!\nYou survived!")
            break
else:
    print("You are hanged!")
