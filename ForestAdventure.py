

last_scene = []


def trail():
    print '-' * 20
    print 'Your car broke down and are now walking down a dark forest \n'
    print 'There is a fork in the trail. Do you go "left" or "right"?'

    direction = raw_input('>').split()

    if 'left' in direction:
        last_scene.append(0)
        return goon1()
    elif 'right' in direction:
        last_scene.append(0)
        return lair()
    else:
        last_scene.append(0)
        print "INPUT INCOMPREHENDABLE"
        return trail()



def goon1():
    last_scene.append(2)
    print '\n\n\n\n', ('-' * 20)
    print 'You proceed down the left fork. \n'
    print 'All of a sudden, an obese platypus jumps out of the trees, blocking your path.'
    print ' QUICK!! Do you blast the platypus or attempt to seduce it? \n'

    choice = raw_input('>').split()

    if "blast" in choice:
        print "The platypus's retinas starts to vaporize, as it twirls around and starts \n eating itself."
        return lair()
    elif "seduce" in choice:
        print "The platypus slaps your face off. Good job!"
        return death()

    else:
        print "INPUT INCOMPREHENDABLE"
        return goon1()

def lair():
    print '\n\n\n\n', ('-' * 20)
    print "You continue walking down the forest. You are freezing and in dire \n need of shelter."
    print "All of a sudden, you come across a secret lair deep in the forest."
    print "As soon as you walk in, the large steel doors shut behind you. \n There is no turning back."
    print 'There are 2 hallways on front of you. Do you go "left" or "right"?'

    hallway = raw_input('>')

    if 'left' in hallway:
        last_scene.append(1)
        return trap_room1()
    elif 'right' in hallway:
        last_scene.append(1)
        return goon20()
    else:
        last_scene.append(1)
        print "INPUT INCOMPREHENDABLE"
        return lair()

def trap_room1():
    last_scene.append(5)
    print '\n\n\n\n', ("-" * 20)

    print """You walk down the hallway, and with every footstep the hallway \n
    becomes more and more eerie. You hear something slithering behind you, \n
    but everytime you turn around, the slithering stops. You quicken your pace,
    only to hear the slithering get closer and closer. You run through \n
    a door on the side of the hallway and shut it behind you.
    You hear a rumble, and the walls \n
    start to close in on you. \n You find a terminal, and must enter a 3 number \n
    code to escape the room. Type in the 3 number code. \n\n **HINT** each number is the product of the previous number and its square."""

    code1 = raw_input('First Number>>')
    code2 = raw_input('Second Number>>')
    code3 = raw_input('Third Number>>')

    if code1.isdigit() != True:

        print "ERROR. You failed to enter a NUMBER."
        return death()

    elif code2.isdigit() != True:
        print "ERROR. You failed to enter a NUMBER."
        return death()
    elif code3.isdigit() != True:
        print "ERROR. You failed to enter a NUMBER."
        return death()

    else:
        pass

    digit1 = int(code1)
    digit2 = int(code2)
    digit3 = int(code3)


    if digit2 == digit1 * (digit1 * digit1) and digit3 == digit2 * (digit2 * digit2):
        print '''BZZZZZZZT. You narrowly avoided death. \n The door has opened and you continue down the hallway.'''
        return goon21()

    else:
        print '''BZZZZZZZT. The code is incorrect. The walls close in and crush \n you to death.'''
        return death()

def goon20():
    last_scene.append(3)
    print '\n\n\n\n', ("-" * 20)
    print """The ceiling above you comes crashing down, and a radicalized octopus
    lays its eyes on you. You look to your left, and you look to your right, only to
    see nothing but the walls of the concrete hallway. You can't run back or the octupus will
    suck you to death with its suckers. The octopus wraps its tentical around you,
    slowly increasing its grip. You can barely breath. \nDo you 'bite' the octopus
    or try to 'negotiate' with it?"""

    action = raw_input('>')

    if 'bite' in action:
        print " You bite off the octopus's tentical, allowing you to escape its grip and run down the hallway."
        return trap_room2()

    elif 'negotiate' in action:
        print "Unfortunately the octopus doesnt know english. The octopus squeezes you until you explode."
        return death()

    else:
        print "INPUT INCOMPREHENDABLE"
        return goon20()

def goon21():
    last_scene.append(4)
    print '\n\n\n\n', ("-" * 20)
    print """The ceiling above you comes crashing down, and a jihadist octopus
    lays its eyes on you. You look to your left, and you look to your right, only to
    see nothing but the walls of the concrete hallway. You can't run back or the octupus will
    suck you to death with its suckers. The octopus wraps its tentical around you,
    slowly increasing its grip. You can barely breath. \nDo you 'bite' the octopus
    or try to 'negotiate' with it?"""

    action = raw_input('>')

    if 'bite' in action:
        print " You bite off the octopus's tentical, allowing you to escape its grip and run down the hallway."
        return gas_hall()

    elif 'negotiate' in action:
        print "Unfortunately the octopus doesnt know english. The octopus squeezes you until you explode."
        return death()

    else:
        print "INPUT INCOMPREHENDABLE"
        return goon21()

def trap_room2():
    last_scene.append(6)
    print '\n\n\n\n', ("-" * 20)

    print """You walk down the hallway, and with every footstep the hallway \n
    becomes more and more eerie. You hear something slithering behind you, \n
    but everytime you turn around, the slithering stops. You quicken your pace,
    only to hear the slithering get closer and closer. You run through \n
    a door on the side of the hallway and shut it behind you.
    You hear a rumble, and the walls \n
    start to close in on you. \n You find a terminal, and must enter a 3 number \n
    code to escape the room. Type in the 3 number code. \n\n **HINT** each number is the product of the previous number and its square."""

    code1 = raw_input('First Number>>')
    code2 = raw_input('Second Number>>')
    code3 = raw_input('Third Number>>')

    if code1.isdigit() != True:

        print "ERROR. You failed to enter a NUMBER."
        return death()

    elif code2.isdigit() != True:
        print "ERROR. You failed to enter a NUMBER."
        return death()
    elif code3.isdigit() != True:
        print "ERROR. You failed to enter a NUMBER."
        return death()

    else:
        pass

    digit1 = int(code1)
    digit2 = int(code2)
    digit3 = int(code3)


    if digit2 == digit1 * (digit1 * digit1) and digit3 == digit2 * (digit2 * digit2):
        print '''BZZZZZZZT. You narrowly avoided death. \n The door has opened and you continue down the hallway.'''
        return gas_hall()

    else:
        print '''BZZZZZZZT. The code is incorrect. The walls close in and crush \n you to death.'''
        return death()

def gas_hall():
    last_scene.append(7)
    print '\n\n\n\n', ("-" * 20)
    print "You continue down and eventually reach the end of the hallway."
    print '''As you turn back, a thick fog engulfs the entire hallway. Each breath feels as if
    you are inhaling  a thousand needles. You see the octopus slithering towards you through the fog. You collapse in agony, suffering with every breath.
    Death appears imminent. Do you "charge towards the octopus" or "accept rahul as your lord and savior"?'''

    choice = raw_input('>')

    if 'charge' in choice:
        print "the octopus shoves the tentical you bit off down your throat. Good Job!"
        return death()

    elif 'accept' in choice:
        print '\n\n\n\n', ("-" * 20)
        print "You wake up on the side of the road, next to the forest with the keys to a brand new Masarati in your hand. \n\nYou get into your new car drive back to civilization. Congratulations!!"
        print '-' * 70
        print 'THE END'







scenes = {
    0: trail,
    1: lair,
    2: goon1,
    3: goon20,
    4: goon21,
    5: trap_room1,
    6: trap_room2,
    7: gas_hall
    }

def death():


    print "You died."
    print "Here is your scene history", last_scene
    print "Type 'RESSURECT' to come back to life"

    ressurection = raw_input('>').split()


    if 'RESSURECT' in ressurection:


        return scenes[last_scene[-1]]()

    else:
        print "You failed to ressurect. Have fun in heaven!"





trail()


#goon21 and traproom2 both go to gas hallway


    #first player chooses to go left or right. If left, encounter goon.
    #if right, enter the lair. goon either kills you or lets u into the lair
    # lair has a fork, left leads you to a room that locks u in, right encounters another goon (then proceed to room that locks you. )
    #u lock urself inside a room, must enter a code to get out (each # is the square of the other, in ascending order from left to right)
    #split input, dont hardcode a single successful password, try to make it formula based
    # 3 tries for password. If FAIL you get run over by a rogue prius. else proceed to trap rooom
    # walls close in. either pray, accept rahul as your lord and savoir, or attempt to hack the mainframe
    # randomly pick a death message from a list
v = '''scenes = {0: 'trail',
    1: 'lair',
    2: 'goon1',
    3: 'goon2',
    4: 'code',
    5: 'trap_room',
    6: 'death',
    7: 'finished'
    }'''
