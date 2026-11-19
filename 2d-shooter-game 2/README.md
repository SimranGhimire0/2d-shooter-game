# Archer vs. Pirates

A 2D arcade game written in Python for CSC 201. Play as an archer defending a ship from approaching pirates.

## Run locally

You’ll need Python 3 with Tkinter and a desktop environment. Keep the Python files and GIF assets together in the same folder.

From that folder, run:

```bash
python3 game.py
```

If Python reports that Tkinter is missing, run `python3 -m tkinter` to check whether your Python installation has GUI support.

## Controls and scoring

- Click the instructions window to continue. Click the game window to start.
- Click to the left or right of the archer, at the archer’s height, to move.
- Press **Space** to fire an arrow.
- Gain a point for each pirate hit. Lose a point when a pirate gets past you.
- Reach **20 points** to win. If a pirate touches the archer, the game ends.

## How the game works

The main loop polls for mouse and keyboard input, spawns pirates at randomized positions, and updates movement and scoring. Collision checks compare the distance between sprites against a threshold. Arrows and pirates are removed when they leave the play area. Separate timed win and loss screens animate balloons or falling pirates.

## Credits

- **Course project:** Binayak and Simran Ghimire.
- **Graphics library:** `graphics2.py` is based on John Zelle’s Tkinter graphics library. See the file header for its GPL notice and the library’s modification history.
- **Artwork:** The GIFs come from the original course-project archive. The archive does not identify their creators or redistribution terms.
