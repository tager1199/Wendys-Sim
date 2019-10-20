# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[playername]")
define main = Character("Wendy")
define friend = Character("Hayley")
$ wendys = 0
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
    if gametime > 7:
            scene bg stairs
            "As you descend the stairs theres a knock at the door"
            scene bg hall
            show friend
            "It's your best friend Heyley. She's just burst through the door!"
            friend  "What took you so long? Come on lets go!"
            scene outside
            jump Out
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
    e "Ah it feels good to be up and about!"
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

label Out:
    "Hayley drags you outside and towards the town"
    scene outtown
    if gametime < 12:
        friend "Come on lets go to the park"
        scene parkfull
        "You play at the park for a few hours before its time to go for lunch"
        scene parkempty
    show friend
    friend "Where do you want to go for lunch? I'm feeling like some fast food."
    menu:
         "Where do you want to go for lunch?"
         "McDonalds":
             $ mcdonalds = True
             $ wendys -= 2
             friend "McDonalds sounds great, let's go!"
             jump mcdonaldslunch

         "Wendys":
             $ wendys =+ 1
             friend "Wendys! I LOVE Wendys!"
             jump wendyslunch
         "Go home to make something":
             friend "Really? if you're sure!"
             jump homelunch




label wendyslunch:

label mcdonaldslunch:
    scene mcdonalds
    show friend
    friend "What are you getting? I'm getting some chicken nugs!"
    menu:
         "What are you ordering?"
         "McChicken Sandwich":
             "Hayley seems pleased with your choice"
         "Filet-O-Fish":
             "Hayley seems dissapointed with your choice"
         "Big Mac":
             "Hayley seems pleased with your choice"
         "Salad":
             "Hayley seems dissapointed with your choice"
    scene mcdonaldstable
    show friend
    friend "Thanks for coming today [playername]. I had a great day"
    scene mcdonaldswendy
    "As you eat and chat with Hayley you notice someone out the window"
    "You realise it's Wendy, the Wendy and she seems to have made eye contact with you!"
    scene mcdonaldstable
    show player
    e "Hey isn't that Wendy out there."
    show friend
    friend "Who?! I cant see anyone."
    show player
    e "Nevermind my mind must have been playing tricks on me."
    "You finish eating and head home, parting from Hayley along the way"
    jump gonehome

label homelunch:


label goneehome:
