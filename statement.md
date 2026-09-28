# Problem Statement

## Problem Statement

Beginners often learn modules, sets, strings and loops separately and rarely see them work together. This project builds a Hangman word guessing game in Python that uses all four in one small, interactive program.

## Scope of the Project

A single player, terminal based Hangman game with:
* Random word selection from a inbuilt list
* Turn based letter guessing with instant feedback
* An ASCII hangman drawing that grows with each wrong guess
* A "play again" option

 ( Not included: multiplayer, saved scores, a graphical interface, or online word sources.)



## Target Users

* Students learning Python basics
* Instructors or evaluators reviewing a simple, readable example
* Anyone wanting a quick game to play in the terminal
  
## High Level Features

* Random secret word each round (random)
* No repeated guesses, tracked with a set
* Input check for single letters only (string)
* Live display of the word, guessed letters and attempts left
* Win/loss detection using a while loop
