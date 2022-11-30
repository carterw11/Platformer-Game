# Platformer-Game
A 2D platformer game made in Python using pygame

## About the game
This program is a 2D platformer game, where the player controls a robot.

When you first open the game, you are shown the home screen, where you can see the controls/a description of the game, upload save files, quit, and start the game. 

### Example of home screen
![image](https://user-images.githubusercontent.com/59629473/204694090-25c540c0-7fc7-4fe5-8717-e9c28235f59d.png)

When you begin the game, you are put into the starting room. To progress the game, you must get to the right side of each room to advance to the next. In rooms, you will encounter enemies and platforming challenges. 

The player has 3 resources, health, energy, and scrap, which can be seen at the top of the screen.

### Example of a room
![image](https://user-images.githubusercontent.com/59629473/204695317-7bcba788-fa14-4490-ba59-2f58b8d61322.png)

Getting hit by enemies makes you lose health, and falling below the screen makes you lose all your health. When your health drops to 0, you return to your last checkpoint and lose half of your scrap. 

### Example of defeat screen
![image](https://user-images.githubusercontent.com/59629473/204696450-6d5eb874-989c-470d-9628-1c73b913f9e0.png)

Scrap is the resource gained from defeating enemies that allows you to purchase upgrades at checkpoints, which are found every 10 rooms.

At checkpoints, you may fully recharge your health and energy, and save your progress to one of three save files.

Saving your progress keeps track of all your upgrades and progress, which can be uploaded on title menu before playing, allowing you to continue from where you left off.

### Example of checkpoint screen
![image](https://user-images.githubusercontent.com/59629473/204695614-a97c3a62-269b-4af7-828e-f07d9bbffede.png)

At checkpoints, you can also purchase upgrades, such as new abilities that cost your energy resource to use, and permanent health and energy.

### Example of shop screen
![image](https://user-images.githubusercontent.com/59629473/204697292-017b8d59-3bef-4958-8c53-69aa9f91fd46.png)

## How to run the game
To run the game, download all the files into the same directory, have all the images in a folder named Images, the saves files in a folder named Saves, and the font in a folder named Fonts.

This game was made on python3, earlier versions may not work.

Make sure to install Pygame.

Then run the python file and enjoy!
