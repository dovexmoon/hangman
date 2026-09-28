# Design Diagrams

All diagrams are written in [Mermaid](https://mermaid.js.org/) syntax.
They render automatically on GitHub, GitLab, and most Markdown
viewers (including VS Code with the "Markdown Preview Mermaid
Support" extension).

---

## 1. System Architecture Diagram

```mermaid
flowchart TB
    subgraph User_Layer["User Layer"]
        Player["Player (Terminal Input/Output)"]
    end

    subgraph App_Layer["Application Layer - hangman.py"]
        WB["Word Bank (WORDS list)"]
        GE["Game Engine (play_game, main)"]
        IV["Input Validator (get_valid_guess)"]
        DR["Display Renderer (display_state, HANGMAN_STAGES)"]
        WC["Win/Loss Checker (is_word_guessed)"]
    end

    subgraph StdLib["Python Standard Library"]
        RND["random module"]
        STR["string module"]
    end

    Player <--> IV
    IV --> GE
    GE --> WB
    GE --> WC
    GE --> DR
    DR --> Player
    WB --> RND
    IV --> STR
```

**Notes:** The game has no external database, network layer, or
third-party services — it is a single self-contained console
application, so the architecture is intentionally simple: one
process, in-memory state only.

---

## 2. Process / Workflow Diagram

```mermaid
flowchart TD
    Start([Start Program]) --> PickWord[Select random secret word]
    PickWord --> Init[Initialize empty guessed-letter set and attempts = 6]
    Init --> ShowState[Display masked word, drawing, attempts left]
    ShowState --> Prompt[Prompt player for a letter]
    Prompt --> Validate{Valid, unused letter?}
    Validate -- No --> Prompt
    Validate -- Yes --> AddSet[Add letter to guessed set]
    AddSet --> InWord{Letter in secret word?}
    InWord -- Yes --> Reveal[Reveal matching letter positions]
    InWord -- No --> Decrement[Decrease attempts left by 1]
    Reveal --> CheckWin{All letters guessed?}
    Decrement --> CheckLoss{Attempts left = 0?}
    CheckWin -- Yes --> WinMsg[Display win message]
    CheckWin -- No --> ShowState
    CheckLoss -- Yes --> LoseMsg[Display loss message and reveal word]
    CheckLoss -- No --> ShowState
    WinMsg --> Again{Play again?}
    LoseMsg --> Again
    Again -- Yes --> PickWord
    Again -- No --> End([End Program])
```

---

## 3. Use Case Diagram

> Mermaid has no native UML use-case shape, so use cases are shown as
> rounded nodes connected to the actor, which is the standard
> workaround for representing use-case diagrams in Mermaid.

```mermaid
flowchart LR
    Actor(["🧑 Player"])
    UC1(("Start New Game"))
    UC2(("Guess a Letter"))
    UC3(("View Game Progress"))
    UC4(("Win Game"))
    UC5(("Lose Game"))
    UC6(("Play Again"))

    Actor --> UC1
    Actor --> UC2
    Actor --> UC3
    Actor --> UC4
    Actor --> UC5
    Actor --> UC6
```

---

## 4. Class / Component Diagram

> The implementation is function-based rather than class-based, so
> this is expressed as a **component diagram**: each box is a
> logical component (a function or group of functions) rather than a
> class with attributes.

```mermaid
classDiagram
    class WordBank {
        +WORDS: list
        +choose_word(word_list) str
    }
    class InputValidator {
        +get_valid_guess(guessed_letters) str
    }
    class DisplayRenderer {
        +HANGMAN_STAGES: list
        +display_state(secret_word, guessed_letters, attempts_left) void
    }
    class WinLossChecker {
        +is_word_guessed(secret_word, guessed_letters) bool
    }
    class GameEngine {
        +MAX_ATTEMPTS: int
        +play_game() void
        +main() void
    }

    GameEngine --> WordBank : uses
    GameEngine --> InputValidator : uses
    GameEngine --> DisplayRenderer : uses
    GameEngine --> WinLossChecker : uses
```

---

## 5. Sequence Diagram

```mermaid
sequenceDiagram
    actor Player
    participant Main as main()
    participant Game as play_game()
    participant WordBank as choose_word()
    participant Validator as get_valid_guess()
    participant Display as display_state()
    participant Checker as is_word_guessed()

    Player->>Main: Run hangman.py
    Main->>Game: play_game()
    Game->>WordBank: choose_word(WORDS)
    WordBank-->>Game: secret_word
    loop While attempts_left > 0 and word not fully guessed
        Game->>Display: display_state(...)
        Display-->>Player: Show masked word + drawing
        Game->>Validator: get_valid_guess(guessed_letters)
        Player->>Validator: Enter letter
        Validator-->>Game: valid letter
        Game->>Checker: is_word_guessed(secret_word, guessed_letters)
        Checker-->>Game: True/False
    end
    Game-->>Player: Display win/loss result
    Main->>Player: Prompt "Play again?"
```

---

## 6. Database / Storage Design

**Not applicable.** This project keeps all state (secret word,
guessed letters, attempts remaining) in memory for the duration of a
single run using a Python `list` and `set`. No file, database, or
persistent storage is used, so no ER diagram or schema design applies.
If a future enhancement adds persistent high scores (see
`PROJECT_REPORT.md`, Future Enhancements), a simple single-table
schema (`player_name`, `words_won`, `date`) would be introduced at
that point.
