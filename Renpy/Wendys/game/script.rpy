# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[playername]")
define main = Character("Wendy")
define friend = Character("Hayley")
define wendys = 0
define date = False
define fuck = False
define wenlunch = False
define mcdonalds = False
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
             $ wenlunch = True
             jump wendyslunch
         "Go home to make something":
             friend "Really? if you're sure!"
             jump homelunch




label wendyslunch:
    $ annoyed = False
    scene wendysinside
    show sexywendy
    main "Hi, how may I help you?"
    "You notice you are being server by Wendy. The Wendy and she looks stunning!"
    show player smart
    menu:
         "What are you ordering?"
         "Barbecue Cheeseburger Double":
             main "Great choice."
         "Homestyle Bacon Jalepeño Chicken":
             main "Great choice. That's my personal favourite!"
             $ wendys += 1
         "Big Mac":
             main "Haha. Very funny"
             "She looks very annoyed"
             $ annoyed = True
             $ wendys -= 2
         "Caesar Side Salad":
             main "Good choice"
    show sexywendy
    main "Thanks for coming. Enjoy your food!"
    scene wendystable
    "You sit down to eat your food"
    show friend
    if annoyed:
        friend "OMG!!! Why were you so rude to her?"
        "You and heyley finish your food in silence before heading home"
        jump gonehome
    friend "OMG!!! SHE'S TOTALY INTO YOU"
    friend "You should ask her out"
    menu:
         "Are you going to ask out Wendy?"
         "Yes!":
             scene wendysinside
             show sexywendy
             main "Hi, Welcome to Wendy's how....."
             main "Oh hi again. How can I help you?"
             menu:
                 "What will you do?"
                 "Just ask her out":
                     show player smart
                     e "Would you like to go out on a date sometime?"
                     show sexywendy
                     if wendys > 3:
                         main "Sure, here's my number. Give me a call sometime."
                         $ date = True
                         jump gonehome
                     main "Sorry, I dont think that would be a good idea."
                     jump gonehome
                 "Use a cheesey pick-up line":
                     show player smart
                     e "Is that burger behind you burning or are you just smokin'"
                     show sexywendy
                     if wendys > 4:
                         main "HaHa. When do you want to meet up?"
                         $ date = True
                         jump gonehome
                     main "Nice line but no thanks."
                     jump gonehome
                 "The earth is a dinosaur":
                     $ wendys += 10
                     main "TAKE ME, RIGHT HERE, RIGHT NOW!"
                     "You and Wendy head back to your house."
                     $ fuck = True
                     jump homefin
         "No":
             friend "Awww! You're sooo boring!"
             "You and heyley finish your food before heading home"
             $ wendys += 1


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
    show player smart
    e "Hey isn't that Wendy out there."
    show friend
    friend "Who?! I cant see anyone."
    show player smart
    e "Nevermind my mind must have been playing tricks on me."
    "You finish eating and head home, parting from Hayley along the way"
    jump gonehome

label homelunch:
    "After some protests from Hayley you convice her to head home for lunch"
    scene outside
    "You both head back to your house and head inside and to the dining room"
    scene bg kitchen
    show friend
    friend "So what are we eating?"
    menu:
         "What are you ordering?"
         "Something Meaty":
             "Hayley seems pleased with your choice"
             friend "The food was great, thanks [playername]. See you tomorrow"
             "You show Hayley out and she heads home."
         "Something Vegetarian":
             "Hayley seems dissapointed with your choice"
             friend "The food was good, thanks [playername]. See you tomorrow"
             "You show Hayley out and she heads home."
         "Something Vegan":
             friend "Really?? I'm just going to eat at my house. See you tomorrow"
             "Hayley storms out and heads home."


label gonehome:
     "After lunch you get on with some work"
     "You've been working for a few hours now and are getting hungry"
     "It's dinner time"
     menu:
         "Where are you going for dinner?"
         "McDonalds":
             $ mcdonalds = True
             $ wendys -= 2
             jump mcdonaldsdinner

         "Wendys":
             $ wendys =+ 1
             jump wendysdinner
         "Stay in and order some pizza.":
             jump homedinner

label wendysdinner:
    if wenlunch == False:
        $ annoyed = False
        scene wendysinside
        show sexywendy
        main "Hi, how may I help you?"
        "You notice you are being server by Wendy. The Wendy and she looks stunning!"
        show player smart
        menu:
             "What are you ordering?"
             "Barbecue Cheeseburger Double":
                 main "Great choice."
             "Homestyle Bacon Jalepeño Chicken":
                 main "Great choice. That's my personal favourite!"
                 $ wendys += 1
             "Big Mac":
                 main "Haha. Very funny"
                 "She looks very annoyed"
                 $ annoyed = True
                 $ wendys -= 2
             "Caesar Side Salad":
                 main "Good choice"
        show sexywendy
        main "Thanks for coming. Enjoy your food!"
        scene wendystable
        "You sit down to eat your food"
        if annoyed:
            "You seem to have annoyed the server"
            "You eat your food and head home"
            jump homefin
        "You seem to think that wendy might be interested in you"
        menu:
             "Are you going to ask out Wendy?"
             "Yes!":
                 scene wendysinside
                 show sexywendy
                 main "Hi, Welcome to Wendy's how....."
                 main "Oh hi again. How can I help you?"
                 menu:
                     "What will you do?"
                     "Just ask her out":
                         show player smart
                         e "Would you like to go out on a date sometime?"
                         show sexywendy
                         if wendys > 3:
                             main "Sure, here's my number. Give me a call sometime."
                             $ date = True
                             jump homefin
                         main "Sorry, I dont think that would be a good idea."
                         jump homefin
                     "Use a cheesey pick-up line":
                         show player smart
                         e "Is that burger behind you burning or are you just smokin'"
                         show sexywendy
                         if wendys > 4:
                             main "HaHa. When do you want to meet up?"
                             $ date = True
                             jump homefin
                         main "Nice line but no thanks."
                         jump homefin
                     "The earth is a dinosaur":
                         $ wendys += 10
                         main "TAKE ME, RIGHT HERE, RIGHT NOW!"
                         "You and Wendy head back to your house."
                         $ fuck = True
                         jump homefin
             "No":
                 "You finish your food before heading home"
                 jump homenull
    show sexywendy
    $ wendys += 1
    main "Fancy seeing you here again"
    main "What can i get you?"
    show player
    e "Same as before please"
    scene wendystable
    "You get the same meal as last time"
    "As you finish you get the urge to ask Wendy out."
    menu:
         "What will you do?"
         "Just ask her out":
             show player smart
             e "Would you like to go out on a date sometime?"
             show sexywendy
             if wendys > 3:
                 main "Sure, here's my number. Give me a call sometime."
                 $ date = True
                 jump homefin
             main "Sorry, I dont think that would be a good idea."
             jump homefin
         "Use a cheesey pick-up line":
             show player smart
             e "Is that burger behind you burning or are you just smokin'"
             show sexywendy
             if wendys > 4:
                 main "HaHa. When do you want to meet up?"
                 $ date = True
                 jump homefin
             main "Nice line but no thanks."
             jump homefin
         "The earth is a dinosaur":
             $ wendys += 10
             main "TAKE ME, RIGHT HERE, RIGHT NOW!"
             "You and Wendy head back to your house."
             $ fuck = True
             jump homefin
         "Just leave":
              jump homefin


label mcdonaldsdinner:
    scene mcdonalds
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
    scene mcdonaldswendy
    "As you eat and chat with Hayley you notice someone out the window"
    "You realise it's Wendy, the Wendy and she seems to have made eye contact with you!"
    scene mcdonaldstable
    show player smart
    e "You think she must have been judgin you on your food choices."
    "You finish eating and head home"
    jump homefin

label homedinner:
    "You order the pizza and put a film on while you wait"
    scene bg living
    "You see Wendy walk past through your window."
    if wenlunch:
        menu:
             "Do you invite Wendy in for pizza and a film?"
             "Yes":
                 scene outside
                 show player
                 e "Hey Wendy, Do you want to come in for pizza and a film?"
                 show sexywendy
                 if wendys > 5:
                      main "Sure, that sounds great"
                      $ fuck = True
                      jump homefin
                 if wendys > 3:
                     main "Sure, that sounds great"
                     $ date = True
                     jump homefin
                 "No sorry, I wouldnt be comfortable with that."
             "No":
                 jump homefin

label homefin:
    scene bg room
    if fuck:
        show wendybed
        main "Lets do this"
        "You and Wendy go to bed together and have the night of your life"
        return
    if date:
        "You and Wendy are now dating and live happily ever after"
        return
    if mcdonald:
        play music "mcdonald.ogg"
    "The day is over"
    "You head to bed"
    "A cold, empty bed"
    "You are alone forever"
    return
