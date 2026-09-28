import random
import string
WORDS = [
    "python", "hangman", "developer", "keyboard", "computer",
    "function", "variable", "iterator", "generator", "dictionary",
    "algorithm", "programming", "software", "network", "database",
]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
]


def choose_word(word_list):
    return random.choice(word_list).lower()


def display_state(secret_word, guessed_letters, attempts_left):
    attempts_used = MAX_ATTEMPTS - attempts_left
    print(HANGMAN_STAGES[attempts_used])

    masked = " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )
    print(f"Word: {masked}")

    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Attempts left: {attempts_left}\n")


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        return guess


def is_word_guessed(secret_word, guessed_letters):
    return set(secret_word) <= guessed_letters


def play_game():
    secret_word = choose_word(WORDS)
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("=" * 40)
    print("WELCOME TO HANGMAN ✌️")
    print("=" * 40)
    print(f"The word has {len(secret_word)} letters. Good luck!\n")

    while attempts_left > 0 and not is_word_guessed(secret_word, guessed_letters):
        display_state(secret_word, guessed_letters, attempts_left)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"'{guess}' is in the word!\n")
        else:
            attempts_left -= 1
            print(f"'{guess}' is not in the word.\n")

    # Final state
    if is_word_guessed(secret_word, guessed_letters):
        display_state(secret_word, guessed_letters, attempts_left)
        print(f"🎉 Congratulations! You guessed the word: '{secret_word}'")
    else:
        print(HANGMAN_STAGES[MAX_ATTEMPTS])
        print(f"💀 Game over! The word was: '{secret_word}'")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Hangman.👋🏻BYE!")
            break
        print()


if __name__ == "__main__":
    main()
