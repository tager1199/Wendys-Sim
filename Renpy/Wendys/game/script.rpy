# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[playername]")
define narrator = Character("")
define main = Character("Wendy")

# The game starts here.


label start:
    $ playername = renpy.input("What is your name")
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show player happy

    # These display lines of dialogue.
    narrator "You've just woken up! It's 9AM and your alarm is beeping"

    narrator "It's a new day, what will you make of today?"

    menu:
         "What should I do?"

         "Hit the snooze button.":
             "You hit the snooze button and go back to sleep."
             jump Sleep

         "Get up and ready":
             "I drink the tea, trying not to make a political statement as I do."
             jump GetUp


    # This ends the game.


    return

label Sleep:

    narrator "After having my drink, I got on with my morning."

label GetUp:

    narrator "After having my drink, I got on with my morning."
