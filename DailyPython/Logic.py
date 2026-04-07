import random

words = ["python", "coding", "chatgpt", "algorithm", "debug"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Enter a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
