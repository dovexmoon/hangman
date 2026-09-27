# Hangman Word-Guessing Game

## Overview

A console-based Hangman game written in Python. The program randomly
selects a secret word, tracks guessed letters using a `set`, and
runs a loop that continues until the player either reveals the word
or runs out of attempts. It was built to demonstrate practical,
combined use of Python modules, sets, strings, and loops.

See [`statement.md`](statement.md) for the full problem statement,
scope, and target users, and [`docs/diagrams.md`](docs/diagrams.md)
for the system architecture, workflow, and UML diagrams.

## Features

- Random word selection on every round
- Duplicate-guess prevention via a `set` of guessed letters
- Input validation (single alphabetic characters only)
- Live ASCII hangman drawing that updates with each wrong guess
- Clear win/loss detection and replay flow
- Unit tests covering word selection and win-condition logic

## Technologies / Tools Used

- **Language:** Python 3.7+
- **Standard library modules:** `random`, `string`
- **Testing:** `unittest` (built into Python — no extra install)
- **Version control:** Git / GitHub
- **Diagrams:** Mermaid (rendered directly in Markdown)

No third-party/pip dependencies are required.

## Project Structure

```
hangman-project/
├── src/
│   └── hangman.py          # Game logic and entry point
├── tests/
│   └── test_hangman.py     # Unit tests (unittest)
├── docs/
│   └── diagrams.md         # Architecture, workflow, and UML diagrams
├── statement.md             # Problem statement, scope, target users
├── README.md                 # This file
└── PROJECT_REPORT.md         # Full project report
```

## Requirements

- Python 3.7 or later
- No external dependencies (standard library only)

## Steps to Install & Run

### 1. Verify Python is installed

```bash
python3 --version
```

If it's missing, install it from [python.org](https://www.python.org/downloads/).

### 2. Get the project

```bash
git clone <your-repository-url>
cd hangman-project
```

(If you received the files as a folder instead of a Git repo, just
`cd` into that folder.)

### 3. (Optional) Create a virtual environment

Not required — there are no dependencies — but good practice:

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 4. Install dependencies

None needed. Skip this step.

### 5. Run the game

From the project root:

```bash
python3 src/hangman.py
```

(Use `python` instead of `python3` on Windows if needed.)

### 6. How to play

1. The program picks a random word and shows blanks for each letter.
2. Type a single letter and press **Enter** to guess.
3. Correct guesses fill in the matching blank(s); incorrect guesses
   reduce your remaining attempts and add another part to the
   hangman drawing.
4. Win by revealing the whole word before attempts run out; lose if
   the drawing is completed first.
5. Choose `y`/`n` to play again or exit.

## Instructions for Testing

Unit tests live in `tests/test_hangman.py` and use Python's built-in
`unittest` framework — no extra installation needed.

Run all tests from the project root:

```bash
python3 -m unittest discover -s tests -v
```

You should see 8 tests pass, covering:
- Word bank integrity (non-empty, lowercase, alphabetic)
- Random word selection returning a valid word
- Win-condition detection (`is_word_guessed`) under multiple
  scenarios (full match, partial match, empty guesses, extra
  irrelevant guesses)
- Configuration sanity (`MAX_ATTEMPTS` is positive)

## Screenshots

See `PROJECT_REPORT.md` → **Screenshots / Results** for a captured
sample terminal run (text-based, since this is a console application).

## Version Control

This project is structured to be tracked with Git:

```bash
git init
git add .
git commit -m "Initial commit: Hangman game with docs and tests"
```

A `.gitignore` is included to keep virtual environments and cache
files out of version control.
