# Project Report

## 1. Cover Page

- **Project Title:** Hangman Word Guessing Game
- **Course/Subject:** VITyarthi Project
- **Student Name:** AAYUSHI SINGH
- **Registration Number:** 26BCE10040
- **Submission Date:** 30th September
- **Repository Link:** https://github.com/dovexmoon/hangman

---

## 2. Introduction

Hangman is a game where the player guesses a hidden word one letter at a time. Each wrong guess adds a body part to a hanging man, and the player loses when the drawing is complete. This project builds the game in Python and runs in the terminal.

## 3. Problem Statement

Beginners learn modules, sets, strings and loops separately and rarely see them working together. This project uses one small, fun game to show all four in a single working program. More detail is in ['statement.md.'] statement.md

## 4. Functional Requirements

The system is organized around three major functional modules:

1. **Word Selection & Game Setup**
   * Input: A fixed word list in code.
   * Output: One randomly chosen secret word and a new game state (blanks for guessing letter set, full attempt
     count).
   * Implemented by `choose_word()` and the setup portion of
     `play_game()`.

2. **Guess Processing & Validation**
   * Input: Keyboard input from the player.
   * Output: A confirmed, valid, previously unused letter added to
     the blank set; or reprompt on invalid input.
   * Implemented by `get_valid_guess()`.

3. **Progress Display & Outcome Reporting**
   * Input: current secret word, guessed letters, and attempts left.
   * Output: the hangman drawing, masked word, guessed letter
     list, attempts remaining, and the final win/loss message.
   * Implemented by `display_state()`, `is_word_guessed()`, and the
     reporting portion of `play_game()`.

The user workflow is: **launch -> guess repeatedly -> see progress
after every guess -> win or lose -> optionally play again.** This
workflow is documented visually in
[`docs/diagrams.md`](../docs/diagrams.md).

## 5. Non-Functional Requirements

| # | Requirement | How it's addressed |
|---|---|---|
| 1 | **Usability** | Clear prompts, a visible progress display after every turn, and plain language error messages for invalid input. |
| 2 | **Reliability** | The game loop's exit condition (`attempts_left > 0 and not is_word_guessed(...)`) guarantees the program always terminates in a win or loss state , no infinite loops or undefined states. |
| 3 | **Error Handling** | `get_valid_guess()` rejects empty input, multicharacter input, non alphabetic characters, and repeated guesses, reprompting instead of crashing. |
| 4 | **Maintainability** | Logic is split into small, single purpose functions with docstrings, making the code easy to read, test, and extend. |
| 5 | **Performance** | Guessed letter lookups use a `set`, giving O(1) membership checks regardless of word length. |
| 6 | **Resource Efficiency** | No external dependencies, network calls, or persistent storage :the program has a minimal memory and runtime footprint. |

## 6. System Architecture

This is a standalone Python console game. It runs entirely offline without internet or databases. It uses standard Python tools to power five core modules: a word bank, game engine, input validator, display renderer, and win/loss checker. For a full visual layout, check the System Architecture Diagram in 
[`docs/diagrams.md`](../docs/diagrams.md),.

## 7. Design Diagrams

All diagrams are provided as flowchart diagram in
[`docs/diagrams.md`](../docs/diagrams.md):

* Workflow Diagram
* Use Case Diagram
* Sequence Diagram
* Class / Component Diagram

## 8. Design Decisions & Rationale

* Set for guessed letters: it stops duplicates and checks quickly.
* Word list inside the code: no setup or internet is needed.
* Functions instead of classes: the game is small, so functions are simpler.

## 9. Implementation Details

* Modules: random.choice() picks the word, and string.ascii_lowercase checks input.
* Sets: guessed_letters stores guesses, and the win check compares the word's letters with this set.
* Strings: the word is shown with _ for unknown letters.
* Loops: a while loop runs each round until the word is guessed or attempts reach 0.

The unchanged source code is in [`src/hangman.py`](../src/hangman.py).

## 10. Screenshots / Results

This is a console application, so results are shown as captured
terminal output rather than graphical screenshots:

```
========================================
   WELCOME TO HANGMAN
========================================
The word has 6 letters. Good luck!

       ------
       |    |
       |
       |
       |
       |

Word: _ _ _ _ _ _
Attempts left: 6

Guess a letter: 'p' is in the word!

       ------
       |    |
       |
       |
       |
       |

Word: p _ _ _ _ _
Guessed letters: p
Attempts left: 6

Guess a letter: 'a' is not in the word.

       ------
       |    |
       |    O
       |
       |
       |

Word: p _ _ _ _ _
Guessed letters: a, p
Attempts left: 5
```

*(Full run truncated for shortness — see `tests/test_hangman.py` output
below for the automated verification.)*

## 11. Testing Approach

Testing combined automated unit tests with manual/scripted
verification:

- **Automated unit tests**
8 unit tests in tests/test_hangman.py
check the word list, word selection and win detection. All pass.
Run them with: python3 -m unittest discover -s tests -v
The game was also played manually, including wrong, repeated and invalid inputs.

## 12. Challenges Faced
* Checking if the whole word is guessed: solved with a set comparison.
* Handling bad input without crashing: solved with a validation loop
## 13. Learnings & Key Takeaways

* Sets are ideal for tracking unique items.
* Small functions are easier to test.
* Planning the workflow first makes coding easier.

## 14. Future Enhancements

* Difficulty levels or word categories
* High-score saving
* A hint feature
* A graphical version

## 15. References

Python documentation: random, string, unittest (docs.python.org)
