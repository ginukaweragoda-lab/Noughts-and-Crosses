# Noughts and Crosses (Tic-Tac-Toe) 🎮

A command-line Tic-Tac-Toe game built in Python, featuring a persistent leaderboard system to track player scores across sessions.

---

## Features

- **Interactive Gameplay** — Play against the computer in a clean terminal interface
- **Score Tracking** — Accumulate scores across multiple games in a single session
- **Persistent Leaderboard** — Save your score and compare with other players via a JSON-backed leaderboard
- **Simple Menu System** — Intuitive options to play, save, view scores, or quit

---

## Project Structure

```
├── noughtsandcrosses.py   # Core game logic and helper functions
├── play_game.py           # Entry point and main game loop
└── leaderboard.txt        # JSON file storing player scores
```

---

## How to Run

Make sure you have **Python 3** installed, then:

```bash
python play_game.py
```

---

## Gameplay

```
1 - Play the game
2 - Save score in leaderboard
3 - Load and display leaderboard
q - Quit
```

- You play as **X**, the computer plays as **O**
- Win → **+1 point** | Draw → **0 points** | Loss → **-1 point**
- Scores accumulate during your session — save anytime!

---

## Leaderboard

Scores are stored in `leaderboard.txt` as JSON and displayed in ranked order:

```
Leaderboard:
Tom: 100
Alix: 75
Hiran: 50
...
```

---

## Technologies Used

- **Python 3** — Core language
- `random` — Computer move generation
- `json` — Leaderboard persistence
- `os.path` — File existence checks

---

## Future Improvements

- [ ] Implement an unbeatable AI using the Minimax algorithm
- [ ] Add a graphical interface (Tkinter or Pygame)
- [ ] Support multiplayer mode
- [ ] Track win/loss/draw statistics separately

---

## Author

Made with ♟️ and Python.
