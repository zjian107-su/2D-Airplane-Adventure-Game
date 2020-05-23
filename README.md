<div style="background-color:#f5f0ff;"># 2D Airplane Adventure Game

Daniel Zezheng Jiang has created a 2D airplane adventure game with Python(3.7.6) and PyGame(2.0.0.dev6) module.

It includes 300 lines of code. It requires the installation of Python and PyGame module in the local machine. 

## **Introduction**

### Getting Started 
1. Create a directory named "**PyGame-Daniel**" on desktop 

2. Open "Terminal"(Linux/MacOS) or Ubuntu(WSL on windows) or [Git](https://git-scm.com/downloads) within the new directory. 

3. Copy the code `$ git clone https://github.com/zjian107-su/2D-Airplane-Adventure-Game.git` into the terminal and press "ENTER"  
   
4. Ensure Python is installed by running `$ python --version` and press "ENTER". If your Python version is below 3.7.7, it is recommanded to [install version 3.7.7](https://www.python.org/) because it's a faster version of Python.
   
5. Create an isolated Python environment with [**Pipenv**](https://pipenv.pypa.io/en/latest/) module. But before that, you need to install it. Within the cloned folder named **2D-Airplane-Adventure-Game**
   ```
   $ brew install pipenv
   $ cd 2D-Airplane-Adventure-Game
   $ pipenv --three
   $ penv install
   $ pipenv shell
   ```

6. Install PyGame module for Python by running `$ pipenv install pygame==2.0.0.dev6`
   
7. Double check if the PyGame is installed corretly by running `$ pipenv run pip freeze`. If you see PyGame listed, then congrats!
   
8. Lastly run `Python3 2D_AirplaneGame.py` and enjoy!

### Basic Navigation In The Game 

Press "A", "W", "D", "S" or any direction key to move the hero airplane. Press space key to shoot bullets. 

A Collision with an enemy airplane or a bullet would end the game. The player may click the "Restart" button to restart the game, and the player may clock the "Quit" button or "X" in the corner of the window to quit.


### Screenshots 
<!--
![Hero Airplane is shoting](screenshots/shooting.png?raw=true "Hero Airplane is shoting")

![End of The Game](screenshots/end.png?raw=true "End of The Game")
-->

![image](https://user-images.githubusercontent.com/35544956/67647936-403c2100-f8f1-11e9-9fbd-220de461124d.png?raw=true "Hero Airplane is Firing")

![image](https://user-images.githubusercontent.com/35544956/67647886-0d922880-f8f1-11e9-82fc-998f4c163a16.png?raw=true "End of The Game")

</div>
