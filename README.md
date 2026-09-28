# Hangman Word-Guessing Game

## Overview

This is a console based Hangman game written in Python. The program randomly
selects a secret word, tracks guessed letters using a `set`, and
runs a loop that continues until the player either guesses the word
or runs out of attempts. It demonstrates practical,
combined use of Python modules, sets, strings, and loops.

Refer [`statement.md`](statement.md) for the full problem statement,
scope, and target users, and [`docs/diagrams.md`](docs/diagrams.md)
for the  workflow.

## Features

-> Random word selection 
-> Duplicate guess prevention using a `set` of guessed letters
-> Single alphabetic characters only
-> Live hangman drawing that updates with each wrong guess
-> Clear checking of win or loss and replay flow
-> Unit tests covering word selection and win/loss logic
-> Limited number if attempts

## Technologies / Tools Used

-> Python 3
-> random module
-> Python set data structure

## Project Structure

```
hangman-project/
├──> src/
│   ──> hangman.py          # Game logic and entry point
├──> tests/
│   ──> test_hangman.py     # Unit tests (unittest)
├──> docs/
│   ──> diagrams.md         # Workflow
├──> statement.md             # Problem statement, scope, target users
├──> README.md                 # This file
└──> PROJECT_REPORT.md         # Full project report
```

## Requirements

-> Python 3.7 or later
-> Standard library only


###  How to play

1. The program picks a random word and shows blanks for each letter.
2. Type a single letter and press **Enter** to guess.
3. Correct guesses fill in the matching blank(s) and incorrect guess
   reduces your remaining attempts and add another part to the
   hangman drawing.
4. Win by guessing the whole word before attempts run out; lose if
   the drawing is completed first.
5. Choose `y`/`n` to play again or exit.

## For Testing

Unit tests live in `tests/test_hangman.py` and use Python's built-in
`unittest` framework.

Run all tests from the project root:

```bash
python3 -m unittest discover -s tests -v
```

You will see 8 tests pass, covering:
-> Word bank integrity (non-empty, lowercase, alphabetic)
-> Random word selection returning a valid word
-> Win-condition detection (`is_word_guessed`) under multiple
  scenarios (full match, partial match, empty guesses, extra
  irrelevant guesses)
-> Configuration sanity (`MAX_ATTEMPTS` is positive)

## Screenshots

Refer `PROJECT_REPORT.md`  **Screenshots / Results** for a captured
sample terminal run .

## Version Control

This project is structured to be tracked with Git:

```bash
git init
git add .
git commit -m "Initial commit: Hangman game with docs and tests"
```

A `.gitignore` is included in this project to keep virtual environments and cache
files out of version control.
