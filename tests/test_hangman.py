import os
import sys
import unittest

# Make src/hangman.py importable without altering hangman.py itself
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from hangman import (  # noqa: E402
    WORDS,
    MAX_ATTEMPTS,
    choose_word,
    is_word_guessed,
)


class TestWordBank(unittest.TestCase):
    def test_words_list_not_empty(self):
        self.assertGreater(len(WORDS), 0)

    def test_words_are_lowercase_alpha(self):
        for word in WORDS:
            self.assertTrue(word.isalpha())
            self.assertEqual(word, word.lower())

    def test_choose_word_returns_word_from_list(self):
        for _ in range(20):  # sample multiple times since it's random
            word = choose_word(WORDS)
            self.assertIn(word, WORDS)


class TestWinCondition(unittest.TestCase):
    def test_is_word_guessed_true_when_all_letters_present(self):
        secret = "python"
        guessed = set("python")
        self.assertTrue(is_word_guessed(secret, guessed))

    def test_is_word_guessed_false_when_letters_missing(self):
        secret = "python"
        guessed = {"p", "y", "t"}
        self.assertFalse(is_word_guessed(secret, guessed))

    def test_is_word_guessed_false_on_empty_guess_set(self):
        secret = "python"
        guessed = set()
        self.assertFalse(is_word_guessed(secret, guessed))

    def test_is_word_guessed_ignores_extra_guessed_letters(self):
        # Guessing extra, irrelevant letters shouldn't break detection
        secret = "cat"
        guessed = {"c", "a", "t", "z", "q"}
        self.assertTrue(is_word_guessed(secret, guessed))


class TestConfig(unittest.TestCase):
    def test_max_attempts_is_positive(self):
        self.assertGreater(MAX_ATTEMPTS, 0)


if __name__ == "__main__":
    unittest.main()
