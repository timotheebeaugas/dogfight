# 2D video game 
Project based on the video series "Creating a Python Game" by YouTube channel Graven  
https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR

The game is very simple. The player starts the game with the `Enter` key and controls a fighter plane with the `directional arrows`. He must fire missiles with the `Space` key to destroy enemies, avoid collisions and must protect airliners. To quit the game just press `Esc`.  
This project uses Python `3.9.0`.

### Project description

    .
    ├── assets                 # Media: images, sounds, font
    ├── aircraft               # Enemy's planes
    ├── airliner               # Civil aircraft
    ├── game                   # Overall game operation
    ├── main.py                # Launch of the game
    ├── menu.py                # Game menus
    |── missile.py             # Player's missile
    |── plane.py               # Player's plane
    |── requirements.txt       # Packages required for the program
    |── rocket_event.py        # Event between levels
    ├── rocket.py              # Enemy rockets 
    ├── sound.py               # Triggering background music and sounds
    └── README.md


### Install packages 
```
pip install -r requirements.txt 
```
### Run the game 
```
python main.py
```

