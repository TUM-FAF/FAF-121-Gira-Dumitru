IDE LABORATORY WORK #2
======================

GUI Development
---------------

<br>
##Completed Tasks
######Laboratory work is done using the cross-platform GUI toolkit Qt, with PyQt bindings and Eclipse IDE with PyDev plugin

   - **Define 3 virtual tasks that you Simulatron is supposed to control**

     - Player can move along of an area, with keyboard.
      The area represents a `QGraphicsScene()` with a `QPixmap()` on it. In the event `keyPressEvent(event)` are managed the cases, so player can move the ship, using `W, A, S, D` keys.
     - Player can destroy all the enemies. 
      By pressing `DEL` key, enemies are destroyed. I've figured too late how to detect the collission between a player and an enemy.
      The idea is that I have to use a holder (QLabel) for every pixmap.
     - Player's time is limited, so game isn't infinite.
      A timer is implemented using `QTimer()`. So when time is up, there is a MessageBox that pop-ups.

   - **Create a GUI application with 5 standard controls**

I've used the following types of standard controls: `QLabel(), QLineEdit(), QPushButton(), QGraphicsView()`.<br>
`QLabel()` is a widget that displays a text or an image. <br>
`QLineEdit()` is a one line text editor. (used to input the player's name)
`QPushButton()` as name implies, is a pushbutton. (used to input and delete player's name, to reset some states)
`QGraphicsView()` is a widget that displays content from a scene. (used for defining the playable area)

   - **Add 3 non-standard controls(2pt)**

     - Pixmaps have been added. For example the player and enemies models. In order to do this, `QPixmap()` class has been used with `addScene()` function applied on scene.
     - Timer included. When player presses `Submit` button, the countdown timer starts. Created with `QTimer()` class and `start()` function.
     - Pop-uping messagebox. When player is trying to close the application, or the time is up, or to delete player's name in game - a messagebox pop-ups. This has been done using `QMessageBox()` class

   - **Make controls to interact. At least 3 interactions (1pt)**

     - When player presses `Submit` button, the text from `QLineEdit()` is copied to a `QLabel()` which shows player's name.
     - When player presses `Submit` button, the countdown timer starts.
     - When player presses `Delete` button, if the player is active - a message box appears, otherwise the name is cleared.
     - If player is moving along the scene, the score(sometimes highscore) is changing.

   - **Create a Reset button. On clicking this button all controls should go to their default state (1pt)**

Reset button has been created with `QPushButton()` class. When button is clicked the `QLineEdit()` is cleared with `clear()`, the score is set to 0, player's name to empty and timer to its default state  with `setText()`

   - **Set a breakpoint in your application and check variables values at that moment of time (1pt)**

   - **Create an installable application (1pt)**

My installable application followed 2 steps. Firstly I've created a `setup.py` script where I described my module, included all the resources and main .py file. Therefore I've created an executable using `cx_freeze` scripts `python setup.py build`. <br>
After that I've used a already personalized installer, and created my own setup.exe.

   - **Mention your own tasks that you did and claim points for them (max of 5 pt in total)**

     - When Simulatron is started, a playback audio has introduced using `QSound()` and `play()` function.
     - There is a highscore label, which reads from / writes into file.


