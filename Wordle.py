import random

import colorama
from colorama import Fore, Style
colorama.init()

wordlist = []
guesslist = []

def validate(word: str):
    for char in word:
        if word.count(char) > 1:
            return False

    if not word.isascii():
        return False

    return True


def populate_wordlist():
    with open('quickwords.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if validate(line):
                guesslist.append(line)
                wordlist.append(line)

    with open('allwords.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if validate(line):
                guesslist.append(line)

def game():
    word = random.choice(wordlist)

    for i in range(0, 6):
        while True:
            print(f"{Style.BRIGHT}Input Guess:{Style.RESET_ALL}")
            guess = input().lower()
            if guess not in guesslist:
                print(f'{Fore.RED}Word not found in word list, try again:{Style.RESET_ALL}')
            else:
                break

        for index, char in enumerate(guess):
            if word[index] == char:
                print(f'{Fore.GREEN}{char.upper()}{Style.RESET_ALL}', end='')
            elif char in word:
                print(f'{Fore.BLUE}{char.upper()}{Style.RESET_ALL}', end='')
            else:
                print(char.upper(), end='')
        print()

        if word == guess:
            print("Correct!\n")
            break

    else:
        print(f"Out of guesses. The word was {word}. New word:\n")


if __name__ == '__main__':
    populate_wordlist()
    while True:
        game()