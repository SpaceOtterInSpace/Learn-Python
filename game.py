from sys import argv
from sys import exit

script, name = argv

print "Greetings %s! You are about to play to play the game 'Alladin: Cave of Wonders'." % name
print "This text-based adventure-puzzle game was created as a project for the course 'Learn Python the Hard Way'."
print "Hope you have fun playing the game. Controls are listed below:"
print "To move, type: 'n' for north, 'e' for east, 's' for south and 'w' west."
print "type 'take' to take something, 'examine' to look close at something."
print "\n"
#print "For actions: 'take' for take, 'examine' or 'look at' for examine."

def enter():
    print "You stand outside The Cave of Wonders. A giant Tiger's head rises above you."
    print "The tiger, opens its mouth and speaks in a thunderous voice:"
    print '"WHO DISTURBS MY SLUMBER?"'
    print "\n"

    name = raw_input("Give your name > ")
    print '"It is I, %s." you reply.' % name

    print "The tiger speaks: "
    print '"Proceed, %s. Touch nothing but the lamp!"' % name
    print "The tiger opens its mouth, revealing a set of stairs that lead downwards."
    print "You proceed down the stairs into the Cave of Wonders."
    print "\n"
    start()

torch = False
carpet = False
riddle = False
lamp = False

def start():

    global torch

    #print "\n"
    print "You are in a small entrance hall with passageways to the east, west, and north."
    print "A pile of treasure sits in front of the passage to the east."
    print "A torch burns brightly next to the north passageway."

    if carpet and not torch:
        print "The carpet takes the torch next to the passage north passage."
        torch = True
    elif carpet and torch:
        print "The carpet floats next to you, holding the torch."
    else:
        pass

    print "Which way do you go?"

    go = raw_input("> ")

    if "e" in go:
        print "You go east, moving treasure out of the way in order to get to the passage."
        dead("You hear the tiger roar, the cave collapses on you and you die.")
    elif "take" in go:
        dead("You hear the tiger roar, the cave collapses on you and you die.")
    elif "n" in go and not carpet:
        treasure_room()
        #print "Would but can't too dark."
    elif "n" and carpet:
        treasure_room()
    elif "w" in go:
        carpet_room()
    else:
        print "Wat?"
        start()

def carpet_room():

    global carpet

    print '\n'

    if not carpet:
        print "You are in a room that is illuminated by bright white light."
        print "The source of the light is small magic jewel resting on the floor."
        print "You see a colorful carpet resting on the floor in front of a passage way to the East."
        print "You can either approach the passageway, or go south to the entrance hall."
        print "Which way do you go?"

        go = raw_input("> ")

        if "e" in go:
            carpet = True
            print "The carpet springs to life just as you are about to step on it."
            print "It points to itself with its tassle and motions you not to touch it."
            print "Then the carpet floats over to the magic jewel and yanks on it, but the jewel doesn't budge."
            print "Apparently the carpet can touch things that you can't."
            print "It then signals you to lead on."
            carpet_room()
        elif "s" in go:
            start()
        elif "take" in go:
            dead("You hear the tiger roar, the cave collapses on you and you die.")
        else:
            print "Wat?"
            carpet_room()

    else:
        print "You are in a room that is illuminated by bright white light."
        print "The source of the light is small magic jewel resting on the floor."
        print "You can either approach the passageway, or go south to the entrance hall."
        print "The carpet floats next to you."
        print "Which way do you go?"

        go = raw_input("> ")

        if "e" in go:
            treasure_room()
        elif "s" in go:
            start()
        elif "take" in go:
            dead("You hear the tiger roar, the cave collapses on you and you die.")
        else:
            print "Wat?"
            carpet_room

def treasure_room():

    print "\n"

    if not torch:
        print "The room is pitch black. You can't see a thing."
        print "You can either stumble around blindly or go back the way you came."
        print "Which way do you go?"

        go = raw_input("> ")

        if "w" in go or "e" in go or "n" in go:
            print "You move %s blindly in the dark. You suddenly feel your leg brush against something metallic." % go
            dead("You hear the tiger roar, the cave collapses on you and you die.")
        elif "s" in go:
            start()
        else:
            print "Wat?"
            treasure_room()

    else:
        print "The torch lights up the room, revealing treasure on all sides."
        print "There are two visible passageways, one to the west and one to the north."
        print "You can take either of these passageways or go back the way you came to the south."

        if carpet:
            print "The carpet floats next to you, holding the torch."
        else:
            pass

        print "Which way do you go?"

        go = raw_input("> ")

        if "w" in go:
            carpet_room()
        elif "n" in go:
            sphinx_room()
        elif "take" in go:
            dead("You hear the tiger roar, the cave collapses on you and you die.")
        else:
            print "Wat?"
            treasure_room()

def sphinx_room():

    global riddle

    print "\n"
    if not riddle:
        print "You are in a small chamber full of gold and jewels."
        print "You see a closed door a few paces from you to the north."
        print "A statue of a sphinx stands next to the door."
        print "The carpet floats beside you."
        print "You can either approach the door to the north or go back south the way you came."
        print "Which way do you go?"

        go = raw_input("> ")

        if "w" in go or "e" in go:
            print "You can't go that way."
            sphinx_room()
        elif "s" in go:
            treasure_room()
        elif "n" in go:
            print "As you move north, the sphinx statue springs to life and moves in front of the door."
            print "After it settles in front of the door, it speaks:"
            print '"In order to pass through this door, you must answer my riddle. Answer incorrectly and you will die."'
            print "The sphinx poses its riddle:"
            print '"At dawn it creeps on four legs,"'
            print '"At noon it strides on two,"'
            print '"At evening it totters on three legs,"'
            print '"What is this thing, I ask you?"'

            answer = raw_input("give your answer > ")

            if "man" in answer or "human" in answer:
                print "The sphinx smiles and says"
                print '"That is correct. You may proceed." and moves aside.'
                riddle = True
                sphinx_room()
            else:
                print "The sphinx smiles and says"
                print '"Wrong answer. Now you die". It reaches out and touches you.'
                dead("You hear the tiger roar, the cave collapses on you and you die.")

        else:
            print "Wat?"
            sphinx_room()

    else:
        print "You are in a small chamber full of gold and jewels."
        print "You see a closed door a few paces from you to the north."
        print "A statue of a sphinx stands, smiling, next to the door."
        print "The carpet floats beside you."
        print "You can either approach the door to the north or go back south the way you came."
        print "Which way do you go?"

        go = raw_input("> ")

        if "w" in go or "e" in go:
            print "You can't go that way."
            sphinx_room()
        elif "s" in go:
            treasure_room()
        elif "n" in go:
            print "The carpet opens the door for you and you move through it."
            lamp_room()
        else:
            print "Wat?"
            sphinx_room()

def lamp_room():

    global lamp

    print "\n"
    if not lamp:
        print "You find youself in a very dark room, but the torch held by the carpet shows a path leading north."
        print "Looking ahead, you see the path leads to a pedestal at the far end of the room, illuminated by a light source somewhere above."
        print "Sitting on the pedestal is a small object you can't identify."
        print "You can either approach the pedestal or go back the way you came to the south."
        print "Which way do you go?"

        go = raw_input("> ")

        if "n" in go:
            print "You approach the pedestal. You see the object in the light from above."
            print "It's the lamp!"

            take = raw_input("Take it? y or n > ")

            if "y" in take:
                print "Taken."
                lamp = True
                lamp_room()
            elif "n" in take:
                print "You move back from the pedestal."
                lamp_room()
            else:
                print "Wat?"
                pass

        elif "e" in go or "w" in go:
            print "you can't go that way."
            lamp_room()
        elif "s" in go:
            sphinx_room()
        else:
            print "Wat?"
            lamp_room()

    else:
        print "You stand by the pedestal, holding the lamp."
        print "The only way to go is south, the way you came in."
        print "Which way do you go?"

        go = raw_input("> ")

        if "e" in go or "w" in go or "n" in go:
            print "you can't go that way."
            lamp_room()
        elif "s" in go:
            print "As you turn to walk south, you feel your leg brush against something metallic."
            print "You hear the tiger roar. Before you can move to the exit, A pile of boulders falls from above, blocking it."
            cave()
        else:
            print "Wat?"
            lamp_room()


def cave():
    print "\n"
    print "You are in the room in which you found the lamp, which you are currently holding."
    print "The only source of light in the room is the torch that the carpet is holding."
    print "What do you do?"

    do = raw_input("> ")

    #if "n" in do or "s" in do or "e" in do or "w" in do:
        #print "You can't go that way."
        #cave()
    if "examine" in do and "lamp" in do:
        print "A closer look at the lamp reveals writing on it."
        print "The writing says: Rub Me"

        rub = raw_input("Rub the lamp? y or n. > ")

        if "y" in rub:
            genie()
        elif "n" in rub:
            print "You do not rub the lamp."
            cave()
        else:
            print "Wat?"
            cave()
    elif "rub" in do and "lamp" in do:
        print "You rub the lamp for reasons known only to yourself."
        genie()
    else:
        print "That won't do any good."
        cave()

def genie():
    print "\n"
    print "A bright blue light explodes from the end of the lamp, followed by copious amounts of blue smoke."
    print "You hear a deafening peal of laughter and gaze in amazement as the smoke begins to gather into a form in front of you."
    print "After a moment a face and body with arms take shape. It's a genie!"
    print "The genie speaks:"
    print '"WOW! Does it feel good to be outa there! Hey rug man, haven\'t seen you in a couple thow, gimme some tass-al, yeah!"'
    print "The carpet and genie high five."
    print "The genie then turns to you."
    print '"And you must be the guy who rubbed my lamp. AL-right! So what\'le it be master? What\'s you wish?"'

    wish = raw_input("Choose wisely! > ")

    w = 0

    while w != 1:
        if "get out" in wish or "leave" in wish:
            w = 1
            print "The genie laughs heartily and speaks."
            print '"You\'re gettin\' your wish, so siddown!"'
            print "The carpet lies down on the floor and you sit on it."
            print 'The genie takes the carpet by the tassle and speaks:'
            print '"Keep your hands and head inside the carpet! We\'re outa here!"'
            win("You escaped the cave!")
        else:
            print 'The genie looks at you funny and speaks:'
            print '"Hold yer horses there partner, you might wanna think about it."'
            wish = raw_input("Choose wisely! > ")

def win(why):
    print "\n"
    print why, "You win!"
    exit(0)

def dead(why):
    print "\n"
    print why, "Better luck next time."
    exit(0)

enter()