from enemy import *
from player import *
import functions
import explore #not completed

## commands list -- If i missed something or you added some functions,please
##                  fill this array.
commands=["train warrior","stats","fight","reproduction","explore","build wall"]
##NOTE: Explore should be random.

print """
WELCOME CONSOLE BASED AND TURN-BASED GAME - 'TRIBE SIMULATION'

FIRST,YOU START WITH YOUR NAME. \n
"""

name=raw_input(">>")

print """

WELCOME %s !
YOU HAVE A TRIBE WHOSE POPULATION IS 50 HUMAN RIGHT NOW.YOUR ENEMY'S POPULATION HAS 50 HUMAN TOO.

YOU CAN TYPE THESE COMMANDS:

>stats -> for learning anything about your tribe.

>reproduction -> to increase your population. Depends on your tribe's moral

>train warrior -> (it is simple,right?)

>build wall -> (c'mon,don't bother me!)

>fight -> fight against enemy tribe

""" %(name)







