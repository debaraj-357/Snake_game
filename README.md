# Snake Game

## Project Overview

Snake Game is a classic terminal-based Snake game developed using Python.

The game provides continuous snake movement, food collection, snake growth, collision detection, scoring, speed control, pause/resume functionality, high score tracking, and a main menu system.

The project is developed following a real-world software developement workflow, including requirements, design, implementation, testing, bug fixing, documentation, and Git/GitHub version control.

## Features

- Classic grid-based Snake gameplay
- Continuous Snake movement
- W/A/S/D Keyboard controls
- Normal Food and Big Food
- Snake growth after eating food
- Wall collision detection
- self-collision detection
- Score and High Score system
- Automatic speed increase
- Multiple Starting Speed Levels
- Pause and Resume
- Restart game option
- Main Menu
- How to Play Section
- Game Over screen

## Requirements

- Python 3.x
- Windows operating system
- Terminal or Command Prompt
- Git (Optional for version control)

## Installation

1. Clone the repository:

```bash
git clone <repository-url> 
```

2. Navigate to the project directory:

```bash
cd Snake_game
```

3. Create a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/Scripts/activate
```

## How to Run

After activating the virtual environment, run the following command:

```bash
python main.py
```

## Controls 

| Key | Action |
|-----|--------|
| W | Move Up |
| S | Move Down |
| A | Move Left |
| D | Move Right |
| P | Pause / Resume |
| SPACE | Pause / Resume |

## Game Rules

- The snake starts with a length of 3 blocks.
- The snake moves continuously in the selected direction
- The snake cannot immediately reverse its direction.
- Hitting the wall results in Game Over.
- Hitting the snake's own body results in Game OVer.
- Food appears inside the snake's playable area.
- Eating food increases the snake's length.
- The game can be paused and resumed using P or SPACE.

## Scoring System

- Normal Food = +5 points
- Big Food = +10 points
- Every 11th Food is a Big Food.
- The High Score is maintained during the game session.

## Speed System

The player can select a starting speed from 2 to 8.
- Speed 2 = Lowest starting speed
- Speed 8 = Maximum speed

The game automatically increase the speed by 1 after every 50 points.

The maximum speed is 8 and the game will never exceed this speed.

## Project structure 

```text
Snake_game/
│
├── main.py
│
├── game/
│   ├── __init__.py
│   ├── board.py
│   ├── snake.py
│   ├── food.py
│   ├── game.py
│   └── menu.py
│
├── REQUIREMENTS.md
├── README.md
├── .gitignore
└── venv/
```

## Future Improvements 

Possible future improvements include:

- Graphical user interface
- Sound effect and background music
- Multiple game modes
- Online leaderboard
- User accounts and authentication
- Database integration
- Score history
- Improved visual effects
