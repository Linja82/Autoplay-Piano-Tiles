"""
Piano Tiles WP Autoplay V5

The title pretty much sums up the entire program. It will play piano tiles.

@author Linja
@date July 24, 2020 10:03 PM

Link to the game: https://www.microsoft.com/en-ca/p/piano-tiles-wp/9nblggh4njz5?activetab=pivot:overviewtab
BTW I did not make the piano tiles game.

High Score:
A La Claire Fontaine:           394 (July 23, 2020 12:53 AM)
Auld Lang Syne:                 635 (July 23, 2020 1:59 AM)
Beginner Challenge:             2531 (July 23, 2020 1:45 AM)
Di Spagna sono la bella:        20 (July 23, 2020 1:53 AM)
Dreaming of Home and Mother:    569 (July 23, 2020 2:24 AM)
Etude Op.10 No.3:               1288 (July 3, 2020 3:08 AM)
Happy Birthday to You:          74 (July 23, 2020 3:14 AM)
Happy New Year:                 270 (July 23, 2020 3:22 AM)
Elegie Op.3 No.1:               438 (July 23, 2020 11:49 AM)
Etude Op.100 No.2:              51 (July 23, 2020 2:12 PM)
Evening song of the Fisherman:  389 (July 24, 2020 3:39 PM)
Heidenroslein:                  64 (July 23, 2020 11:56 AM)
Inventions No.15:               311 (July 23, 2020 2:09 PM)
Jingle Bells Chirstmas Edition: 599 (July 23, 2020 2:24 PM)
Jingle Bells:                   55 (July 23, 2020 2:25 PM)
Lascia chio pianga:             32 (July 23, 2020 2:31 PM)
Little Star:                    406 (July 23, 2020 2:34 PM)
Londonderry Air:                408 (July 24, 2020 5:20 PM)
"""

import time
import keyboard
import win32gui
import pyautogui

# Variables
y_disp = 600                    # How many pixels below the top of the window the detection will take place
y_click_disp = 75               # How many pixels below the detection the click will take place
longPress = 0.008               # Duration for the long press tiles

# End Screen Colours
endScreen1 = (0, 129, 210)      # Sky blue
endScreen2 = (57, 57, 74)       # Grey line
endScreen3 = (117, 172, 246)    # Baby glue

# Detect initialization command.

wait = True
print("Press F1 to start the program.")
while wait:
    if keyboard.is_pressed("f1"):
        wait = False

print("Press ESC to exit the program.")

# Main loop starts

run = True
while run:

    # Detect exit command

    if keyboard.is_pressed("esc"):                          # If the exit key is detected the main loop will be exited.
        run = False

    # Capture Screenshot

    image = pyautogui.screenshot()                          # Captures and stores a screenshot of the main display
    image_rgb = image.convert("RGB")                        # Converts screenshot to RGB colour values

    # Get window position information

    handle = win32gui.FindWindow(None, "Piano Tiles WP")    # Retrieves the window handle of the game
    X, Y, right, bottom = win32gui.GetWindowRect(handle)    # Retrieves window position coordinates (top left corner (x, y) and bottom right corner (x, y)
    Width = right - X                                       # Calculates window width using the two coordinates
    Height = bottom - Y                                     # Calculates window height using the two coordinates

    # Determine the click position

    y_coord = Y + y_disp                                    # Shifts the detection line below the Y value of the top left corner

    x_coord = (Width / 8) + X                               # Calculates the X value of the 1st column of tiles
    posA = (x_coord, y_coord)                               # Creates a coordinate where the detection will take place
                                                            # for posA. Repeats for all positions.
    x_coord = (Width / 4) + (Width / 8) + X
    posB = (x_coord, y_coord)

    x_coord = (Width / 2) + (Width / 8) + X
    posC = (x_coord, y_coord)

    x_coord = x_coord = Width - (Width / 8) + X
    posD = (x_coord, y_coord)

    # Get colour values from the detection line

    posAColour = image_rgb.getpixel(posA)                   # Sets the variables to the RGB colour values at the 4 pixel
    posBColour = image_rgb.getpixel(posB)                   # positions
    posCColour = image_rgb.getpixel(posC)
    posDColour = image_rgb.getpixel(posD)

    posA_R, posA_G, posA_B = posAColour                     # Creates individual variables for red, green, and blue
    posB_R, posB_G, posB_B = posBColour
    posC_R, posC_G, posC_B = posCColour
    posD_R, posD_G, posD_B = posDColour

    print(posAColour)                                       # Prints the RGB colour values at the 4 pixel positions
    print(posBColour)
    print(posCColour)
    print(posDColour)

    # Determine where to click

    if posAColour == endScreen1 or posAColour == endScreen3:  # Detects if the screen has the colour from the end screen
        run = False                                           # Stops the program
    elif 20 <= posA_R <= 40 and 20 <= posA_G <= 40 and 40 <= posA_B <= 80:      # Detects a long press tile in posA
        x, y = posA
        y += y_click_disp                       # Shifts the click position down from the detection position
        pyautogui.moveTo(x, y, duration=0)      # Moves the mouse
        pyautogui.mouseDown(button='left')      # Holds down left mouse button
        time.sleep(longPress)                   # Preset hold down time
        pyautogui.mouseUp(button='left')        # Releases the left mouse button
        print("Long Click A")
    elif 15 <= posA_R <= 19 and 15 <= posA_G <= 19 and 20 <= posA_B <= 22:      # Detects a short press tile in posA
        x, y = posA
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click(button='left')
        print("Click A")
    elif 20 <= posB_R <= 40 and 20 <= posB_G <= 40 and 40 <= posB_B <= 80:      # Detects a long press tile in posB
        x, y = posB
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.mouseDown(button='left')
        time.sleep(longPress)
        pyautogui.mouseUp(button='left')
        print("Long Click B")
    elif 15 <= posB_R <= 19 and 15 <= posB_G <= 19 and 20 <= posB_B <= 22:      # Detects a short press tile in posB
        x, y = posB
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click(button='left')
        print("Click B")
    elif 20 <= posC_R <= 40 and 20 <= posC_G <= 40 and 40 <= posC_B <= 80:      # Detects a long press tile in posC
        x, y = posC
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.mouseDown(button='left')
        time.sleep(longPress)
        pyautogui.mouseUp(button='left')
        print("Long Click C")
    elif 15 <= posC_R <= 19 and 15 <= posC_G <= 19 and 20 <= posC_B <= 22:      # Detects a short press tile in posC
        x, y = posC
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click(button='left')
        print("Click C")
    elif 20 <= posD_R <= 40 and 20 <= posD_G <= 40 and 40 <= posD_B <= 80:      # Detects a long press tile in posD
        x, y = posD
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.mouseDown(button='left')
        time.sleep(longPress)
        pyautogui.mouseUp(button='left')
        print("Long Click D")
    elif 15 <= posD_R <= 19 and 15 <= posD_G <= 19 and 20 <= posD_B <= 22:      # Detects a short press tile in posD
        x, y = posD
        y += y_click_disp
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click(button='left')
        print("Click D")
    print("")

print("Finish")
