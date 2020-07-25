# Autoplay-Piano-Tiles
A Python script that plays piano tiles.

## Installation Instructions
Necessary Libraries:
- time  
- keyboard  
- win32gui  
- pyautogui  

Download "Autoplay V5". Run the file.

## How It Works
Step 1: Pyautogui takes a screenshot and stores it in memory. The image is then converted to RGB colour values.  
  
Step 2: Win32gui is used to get the location information of the game window. Some calculations are performed to determin where each column of the game is. Based on where each column is a detect position is determined.  
  
Step 3: The RGB colour values are grabbed from the 4 detection pixels.  
  
Step 4: An if block is used to determine where and when a click should take place. The RGB colour values are used to compare with a known range of colours.  

## Game
Here's a link to the game:  
<a href="https://www.microsoft.com/en-ca/p/piano-tiles-wp/9nblggh4njz5?activetab=pivot:overviewtab">Piano Tiles WP</a>  
BTW: I did not make this game. This code just plays the game.

