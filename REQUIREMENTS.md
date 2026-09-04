#Snake Game - Requirements
## 1. Project overview
Snake Game is classic grid-based game developed using python.

The player controls a snakke that continuously moves around the game board. The objective is to eat food, increase the snake's length, score points, and achieve the highest possible score.

THe snake game mst avoid :
- THe walls of the game board
-Its own body

Collision with either the wall or the snake's owen will result in Game OVer.

## 2. Tecchnology
- Programming Language: Python
- Interface: TErminal / Command Line
- External Game Framework: None
- Virtual Environment: venv

## 3. Board and Wall Requirements

## 3.1 Game Board

The game board will have a target visual size of 5 × 5 inches.

The board will use a 30 × 30 square-cell grid.

The border thickness will be approximately 0.3 cm.

The playable area will be inside the border.

The board will have a clearly visible boundary made walls.

The snake, food , and other game elements will be pplaced inside the playable area of the board.

### 3.2 Wall

The wall will act as a boundary the the snake must not touch. 

- Wall colo: Light/Medium Yellow-brown
- Wall Thikness: 0.3 cm
- Wall must be clearly distinguishable from the yellow food.
- The wall must not be too dark
- The wall will surrounded the playable game area.

### 3.3 Wall Collision

If the snake's head touched the wall:

1. A collision will be detected.
2. The game will stop.
3. THe player wi;; recieve a Game Over.
4. The final score will be displayed.
5. The player will have an option to restart or return to the menu.

### 3.4 Food Placement

Food must alwayes appear inside the playaboad area.

Food must not be generated:

- On the wall
- Outside the game board
- On any part of the snake's body

## 4. Snake Requirements

### 4.1 Initial Snake

- THe snake will start with length 3 blocks.
- The snake will start from a valid position inside the game board.
- The snake will have an initial movement direction.

### 4.2 Snake Appearance


- Snake Head: red
- Snake Body: Green

The head must be visually distinguishable from the body.

### 4.3 Continuous Movement 

The Snake will move continuously in its current direction.

The player will control the snake using keyboard controls.

The Snake will move one grid cell at a time.

### 4.4 Direction control

The player will able to change the snake's direction using keyboard controls.

THe snake must not be allowed to immediately reverse its direction.

For example:
- Moving Right -> Cannot immediately move Left
- Movinf Left -> Cannot immediately move Right
- Moving Up -> Cannot immediately move Down
- Moving Down -> cannot immediately move Up

### 4.5 Snake Growth

When the snake eats food:

- The snake's Length will increase.
- A few food will be generated.
- The score will be updated according to the type of food eaten.

### 4.6 Self Collision

If the snake's head touches any part of its own body: 
1. A collision will be detected.
2. THe game will stop.
3. Game over will be displayed.
4. THe final score will be displayed.
THe player will have an option to restart or retuen to the menu.

## 5. Food Requirements

### 5.1 Normal Food

- Color: Yellow
- Score: +5
- Normal food will have the standard food size

When the snake eats normal food:

- The snake will grow.
- The player will recieve 5 points.
- New food will be generated.

### 5.2 Big Food

Every 11th fodd will be a Big Food.

Food sequence:

- Food 1-10 -> Normal Food
- Food 11 -> Big Food
- Food 12-21 -> Normal Food
- Food 22 -> Big Food
- Food 23-32 -> Normal Food
- Food 33 -> Big Food
- The parttern will continue.

Big Food requirements:

- Color: yellow
- Score: +10
- Size: larger the normal food

Bog Food will be visible distinguishable from normal food mainly through its larger size.

### 5.3 Food Spawning

After the snake eats food, a new will be generated.

The new fodd must:

- Appear inside the playable area.
- Not appear in the wall.
- Not appear on the snake's body.

Only one foos item will normal exist on the board at a time.

## 6. Score Requirements 

The game will maintain a sscore for the current game.

Scoring rules:

- Normal Food = +5 pints
- Big Food = +10 points

The score will dislayed duiring the gameplay.

The final Score will be displayed when the game ends.

## 7. High Score Rerquirements

THe game will maintain a local high score.

If the current score is greater than the previous high score:

- THe high score will be updated.
- The game will indicate that a new high score has been achieved.

The high score will be available from the main menu.

The high score will remain available after restarting the game.

## 8. Spped Requirements

THe game will have multiple spped levels.

Available spped levels:
- 2
- 4
- 6
- 8
- 10

Speed 2 will be the lowest spped.

Speed 10 will be the maximum speed.

### 8.1 Starting Spped.

The player will be able to select a starting speed from the available speed levels.

### 8.2 Automatic Speed Increase

During gameplay, the snake's speed will automatically increase as the score increases.

The speed level will increase by 1 at every 50 point milestone.
- Score 0-49 -> Starting speed
- Score 50+ -> Starting speed + 1
- Score 100+ -> Starting speed + 2
- Score 150+ -> Starting speed + 3
- Continue until maximul speed 10.

The speed must never exceed level 10.

## 9. Game Controles

Keyboard controls will be used to control the game.

### Movement 

- Up -> Move Up
- Down -> Move Down
- Left -> Move Left
- Right -> Move Right

### Pause 

-P or SPACE -> Pause / Resume

### Menu

The player will use keyboard input to navigate the menu and select options.

## 10. Main Menu

The game will provide a main menu.

The main menu will contain: 

1. Start Game
2. Select Speed
3. High Score 
4. How to play
5. Exit

The player will be able to select an option using keyboard input.

## 11. pause and Resume

The player will be able to pause the game during gameplay.

When the game is paused:

- Snake movement will stop.
- The game board will remain visible.
- A Pause message will be displayed.

The player can resume the game using the assigned pause/resume key.

## 12. Game Over

Game Over will occure when:

- The snake hits the wall.
- The snake hits its own body.

The Game Over screen will displayed:

- Game Over message
- Final Score
- High Score
- Rrestart Option
- Return to Main Menu Option

## Restart 

The player will be able to restart the game after Game OVer.

When restarting:

- The snake will return to its initial length.
- The score will restart to zero.
- The food counter will reset.
- The select starting speed will be applied again.
- A new game will begin.

## 14. How to play

The game will be provide a How to Play Selection.

It will explain:

- How to control the snake.
- How to eat food.
- Normal Food scoring.
- Big Food scoring.
- Wall Collision.
- Self Collision.
- Pause/ resume controls.
- Basic objecyive of the game

## 15. Exit

The player will be able to exit game from the main menu.

The game will close safely without producing unnecessary errors or leaving the terminal in an unusable state.

## 16. Error and Edge Case Handling

The game should handel important edge cases safely.

Examples:

- Food must not spawn inside inside the snake.
- Food must not spawn on the wall.
- The snake must not immediately reverse direction.
- Speed must not exceed level 10.
- High Score must update correctly.
- Restart menu reset the current game state correctly.
- Invalid menu input not crash the game.

## 17. Project Goal

The goal of this project is to build a complete playable,well-tested, and documented Snake Game using Python.

The project should follow a professional developement workfloe:

Requirements
-> Design
-> Implemention
-> Testing 
-> Bug Fixing
-> Documentation
-> Git/GitHub
-> Release
