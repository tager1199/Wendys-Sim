# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[playername]")
define main = Character("Wendy")
define friend = Character("Hayley")

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
    "You've just woken up! It's 7AM and your alarm is beeping"

    "It's a new day, what will you make of today?"
    $ gametime = 7
    menu:
         "What should I do?"

         "Hit the snooze button.":
             "You hit the snooze button and go back to sleep."
             jump Sleep

         "Get up and ready":
             "You get up, shower and get dressed."
             jump GetUp


    # This ends the game.


    return

label Sleep:

    $ gametime = 12
    "After your extra sleep you wake up at 12PM, half the day is gone."


label GetUp:

    show player smart
    "Now you're up and ready to get on with your day. "
    menu:
         "What are you going to do?"

         "Have a healthy, nutritious breakfast":
             $ breakfast = True
             jump Breakfast

         "Grab a coffee and head out":
             "You drink the coffee, trying not to make a political statement as I do."
             jump OutEarly

label Breakfast:
    scene bg stairs
    show player smart
    "You head downstairs and into your dining room"
    scene bg kitchen
    show player smart
    menu:
         "What are you eating for breakfast?"

         "Porridge with fruits":
             "You enjoy your healthy breakfast."

         "A full English breakfast":
             $ fatty = True
             "You devour the meaty breakfast."
             "You feel you could tow anything."

    scene kitchen knock
    show player smart
    "Suddenly theres a knock at the door"
    scene bg hall
    show friend
    "It's your best friend Heyley. She's just burst through the door!"
    friend  "What took you so long? Come on lets go!"
    scene outside
    jump Out

label OutEarly:
    scene outside
    "You step out the house just as your best friend comes running up"
    show friend
    friend "Hey you're out early, you must be excited. ME TOO!"
    jump Out

label Out:
    "Hayley drags you outside and towards the town"
    scene outtown
    friend "Come on lets go to the park"
    scene park
    "You play at the park for a few hours before its time to go for lunch"
    show friend
    friend "Where do you want to go for lunch? I'm feeling like some fast food."
    menu:
         "Where do you want to go for lunch?"

         "McDonalds":
             $ mcdonalds = True
             friend "McDonalds sounds great, let's go!"
             jump mcdonaldslunch

         "Wendys":
             $ wendys = 1
             friend "Wendys! I LOVE Wendys!"
             jump wendyslunch
         "Go home to make something":
             friend "Really? if you're sure!"
             jump homelunch




label wendysLunch:

label mcdonaldsLunch:

label homeLunch:
