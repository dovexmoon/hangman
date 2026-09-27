# Problem Statement

## Problem Statement

Learning to code is often abstract — beginners read about loops, sets,
and modules without a tangible way to see them work together. There
is a need for a small, self-contained, interactive program that
demonstrates these core Python concepts in a way that is genuinely
fun to use rather than a dry syntax exercise. Hangman is a well-known
word-guessing game that naturally requires random selection, unique
state tracking, string manipulation, and repeated user interaction —
making it a strong practical vehicle for demonstrating these
concepts end-to-end.

## Scope of the Project

This project implements a **single-player, console-based Hangman
game** in Python. It is scoped to:

- Word selection from a fixed, in-code word list (no external
  dictionary/API).
- Turn-based letter guessing with immediate feedback.
- Visual (ASCII) representation of the hangman's progress.
- Replayability within a single program run.

**Out of scope:** multiplayer support, persistent score storage
across sessions, a graphical user interface, and network/API-based
word sources. These are listed as future enhancements rather than
current features.

## Target Users

- Students learning Python fundamentals (modules, sets, strings,
  loops, functions).
- Instructors/evaluators who want a compact, readable example of
  these concepts applied together.
- Casual users who want a quick, dependency-free word game to run
  from a terminal.

## High-Level Features

- Random secret word selection on every round (`random` module).
- Duplicate-guess prevention using a `set` of guessed letters.
- Input validation restricted to single alphabetic characters
  (`string` module).
- Live progress display: masked word, guessed letters, attempts
  remaining, and an ASCII hangman drawing.
- Win/loss detection driven by a `while` loop over remaining
  attempts.
- "Play again" flow to run multiple rounds without restarting the
  program.
