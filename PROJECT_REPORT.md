# Project Report

## 1. Cover Page

**Project Title:** Hangman Word-Guessing Game
**Course/Subject:** [Insert your subject name here]
**Student Name:** [Insert your name here]
**Registration/Roll Number:** [Insert here]
**Submission Date:** [Insert here]
**Repository Link:** [Insert your GitHub repository URL here]

---

## 2. Introduction

Hangman is a classic word-guessing game in which a player tries to
identify a hidden word by guessing one letter at a time, with a
limited number of incorrect guesses allowed before losing. This
project implements Hangman as a console-based Python application. It
was chosen as a project topic because it naturally requires several
core programming concepts — random selection, unique-value tracking,
string processing, and iterative control flow — to work together in
a single, easily demonstrable program.

## 3. Problem Statement

Learners often study programming concepts such as modules, sets,
strings, and loops in isolation, without a small, complete
application that shows them working together toward one goal. This
project addresses that gap by building an interactive word-guessing
game that requires all four concepts to function correctly, giving a
concrete, testable demonstration of each one. Full details, scope,
and target users are documented separately in
[`statement.md`](../statement.md).

## 4. Functional Requirements

The system is organized around three major functional modules:

1. **Word Selection & Game Setup**
   - Input: a fixed in-code word list.
   - Output: one randomly chosen secret word and a freshly
     initialized game state (empty guessed-letter set, full attempt
     count).
   - Implemented by `choose_word()` and the setup portion of
     `play_game()`.

2. **Guess Processing & Validation**
   - Input: raw keyboard input from the player.
   - Output: a confirmed, valid, previously-unused letter added to
     the guessed-letter set; or a re-prompt on invalid input.
   - Implemented by `get_valid_guess()`.

3. **Progress Display & Outcome Reporting**
   - Input: current secret word, guessed letters, and attempts left.
   - Output: the ASCII hangman drawing, masked word, guessed-letter
     list, attempts remaining, and the final win/loss message.
   - Implemented by `display_state()`, `is_word_guessed()`, and the
     reporting portion of `play_game()`.

The user workflow is: **launch → guess repeatedly → see progress
after every guess → win or lose → optionally play again.** This
workflow is documented visually in
[`docs/diagrams.md`](../docs/diagrams.md) (Section 2, Process/Workflow
Diagram).

## 5. Non-Functional Requirements

| # | Requirement | How it's addressed |
|---|---|---|
| 1 | **Usability** | Clear prompts, a visible progress display after every turn, and plain-language error messages for invalid input. |
| 2 | **Reliability** | The game loop's exit condition (`attempts_left > 0 and not is_word_guessed(...)`) guarantees the program always terminates in a win or loss state — no infinite loops or undefined states. |
| 3 | **Error Handling** | `get_valid_guess()` rejects empty input, multi-character input, non-alphabetic characters, and repeated guesses, re-prompting instead of crashing. |
| 4 | **Maintainability** | Logic is split into small, single-purpose functions with docstrings, making the code easy to read, test, and extend. |
| 5 | **Performance** | Guessed-letter lookups use a `set`, giving O(1) membership checks regardless of word length. |
| 6 | **Resource Efficiency** | No external dependencies, network calls, or persistent storage — the program has a minimal memory and runtime footprint. |

## 6. System Architecture

The application is a single-process console program with no external
services, database, or network layer. It consists of an application
layer (word bank, game engine, input validator, display renderer,
win/loss checker) built on top of Python's standard library
(`random`, `string`). See the full **System Architecture Diagram** in
[`docs/diagrams.md`](../docs/diagrams.md), Section 1.

## 7. Design Diagrams

All diagrams are provided as Mermaid diagrams in
[`docs/diagrams.md`](../docs/diagrams.md):

- Section 1 — System Architecture Diagram
- Section 2 — Process / Workflow Diagram
- Section 3 — Use Case Diagram
- Section 4 — Class / Component Diagram
- Section 5 — Sequence Diagram
- Section 6 — Database/Storage Design (marked not applicable, with
  justification, since the game uses only in-memory state)

## 8. Design Decisions & Rationale

- **Function-based design over classes:** the game has a single
  "session" of state at a time and no need for multiple instances or
  inheritance, so plain functions keep the implementation simpler
  and easier to follow than a class hierarchy would.
- **`set` for guessed letters:** chosen over a `list` because guesses
  must be unique and membership needs to be checked on every input —
  a set gives both properties for free with O(1) lookups.
- **In-code word list instead of a file/API:** keeps the project
  fully self-contained with zero setup friction and no network
  dependency, appropriate for the project's scope (see
  `statement.md`).
- **Single loop condition for win/loss:** combining
  `attempts_left > 0` and `not is_word_guessed(...)` into one `while`
  condition avoids duplicated exit checks scattered through the code.

## 9. Implementation Details

- **Modules:** `random.choice()` selects the secret word;
  `string.ascii_lowercase` validates guesses.
- **Sets:** `guessed_letters` is a `set`; win detection uses set
  comparison (`set(secret_word) <= guessed_letters`).
- **Strings:** the masked word is built with a generator expression
  joined by `" "`, substituting `_` for unrevealed letters; all
  input is normalized with `.strip().lower()`.
- **Loops:** the `while` loop in `play_game()` drives each round; a
  `while True` loop in `get_valid_guess()` re-prompts until valid
  input is received; an outer `while True` loop in `main()` supports
  replaying multiple rounds.

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

*(Full run truncated for brevity — see `tests/test_hangman.py` output
below for the automated verification.)*

## 11. Testing Approach

Testing combined automated unit tests with manual/scripted
verification:

- **Automated unit tests** (`tests/test_hangman.py`, run via
  `python3 -m unittest discover -s tests -v`): 8 tests covering word
  bank integrity, random selection validity, and win-condition
  detection across multiple scenarios. All 8 tests pass.
- **Static validation:** the source was parsed with Python's `ast`
  module to confirm there are no syntax errors.
- **Scripted playthrough simulation:** the game was run with piped
  input simulating full guess sequences to confirm the hangman
  drawing progresses correctly, attempts decrement accurately, and
  win/loss messages display the correct word.
- **Manual input-validation review:** confirmed that duplicate
  guesses, non-letter characters, and multi-character input are
  rejected with a re-prompt rather than consuming an attempt or
  crashing.

## 12. Challenges Faced

- Deciding how to represent "all letters guessed" cleanly led to
  using set comparison (`set(secret_word) <= guessed_letters`)
  instead of a manual loop, which simplified `is_word_guessed()`
  considerably.
- Balancing input validation strictness (rejecting bad input) against
  usability (not being overly restrictive or confusing) required
  iterating on the error messages in `get_valid_guess()`.
- Representing UML diagrams for a function-based (not class-based)
  program required adapting the Class/Component and Use Case diagrams
  to fit Mermaid's available diagram types.

## 13. Learnings & Key Takeaways

- Sets are a natural fit whenever "has this been seen before?" needs
  to be answered repeatedly and efficiently.
- Structuring even a small program into single-purpose functions
  makes it dramatically easier to unit test in isolation.
- Writing the workflow diagram before finalizing the report clarified
  a couple of edge cases (e.g., what happens on the exact last
  attempt) that were already handled correctly by the loop condition,
  but hadn't been explicitly reasoned through beforehand.

## 14. Future Enhancements

- Support word categories or difficulty levels.
- Add a persistent scoring/high-score system (would introduce a
  simple storage schema — see `docs/diagrams.md`, Section 6).
- Load the word list from an external file for easier customization
  without editing code.
- Add a hint system (e.g., reveal a letter for a score penalty).
- Build a graphical or web-based front end.

## 15. References

- Python Software Foundation. *`random` — Generate pseudo-random
  numbers.* Python 3 documentation.
- Python Software Foundation. *`string` — Common string operations.*
  Python 3 documentation.
- Python Software Foundation. *`unittest` — Unit testing framework.*
  Python 3 documentation.
- Mermaid. *Mermaid Diagramming and charting tool.*
  https://mermaid.js.org/
