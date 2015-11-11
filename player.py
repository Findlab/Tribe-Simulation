#!/usr/bin/python2.7
# -*- coding: cp1254 -*-


########################################
# TRIBE SIMULATION version 0.0.0.0.0.1
#
#Author:Mert Arıkan (Findlab)
#GitHub: https://github.com/Findlab
#
#
#If you want to add some codes;be my guest :)
#
########################################

import random

class Player:

    def __init__(self):
        self.POP_TRIBE_SICK=0
        self.POP_TRIBE=50 #The population of tribe
        self.TRIBE_RESOURCE={"food":random.randint(20,120),"spear":random.randint(0,self.POP_TRIBE),"wood":random.randint(50,200),"steel":0}
        self.TRIBE_WARRIOR=0
        self.TRIBE_WALLS=False
        self.TRIBE_MINER=0
        self.TRIBE_WOODMAN=0
        self.TRIBE_EXPLORER=0
        self.TRIBE_WINS=0 # Tribe can gain win when they explore something,winnig war...
        self.TRIBE_LOSE=0  # Losing war,the number of sick people...
        self.TRIBE_EXP_LEVEL=0 #Exploring level


        if self.TRIBE_WINS-self.TRIBE_LOSE>=20:
            self.TRIBE_MORAL="WONDERFUL!"
        elif self.TRIBE_WINS-self.TRIBE_LOSE>10 and self.TRIBE_WINS-self.TRIBE_LOSE<20:
            self.TRIBE_MORAL="VERY GOOD!"
        elif self.TRIBE_WINS-self.TRIBE_LOSE<=10 and self.TRIBE_WINS-self.TRIBE_LOSE>5:
            self.TRIBE_MORAL="GOOD!"
        elif self.TRIBE_WINS-self.TRIBE_LOSE<=5 and self.TRIBE_WINS-self.TRIBE_LOSE>0:
            self.TRIBE_MORAL="NOT BAD!"
        elif self.TRIBE_WINS-self.TRIBE_LOSE==0:
            self.TRIBE_MORAL="NEUTRAL"
        else:
            self.TRIBE_MORAL="BAD!!!"


        self.EXPLORE_CHANCE=self.TRIBE_EXPLORER*(2.13)+(self.TRIBE_WINS-self.TRIBE_LOSE)
        self.FIGHT_CHANCE=self.TRIBE_WARRIOR*(2.13)+(self.TRIBE_WINS-self.TRIBE_LOSE)

        if self.TRIBE_WALLS==True:
            self.DEFENCE_CHANCE=25+(self.TRIBE_WARRIOR*(3.14))+(self.TRIBE_WINS-self.TRIBE_LOSE)
        else:
            self.DEFENCE_CHANCE=5+(self.TRIBE_WARRIOR*(3.14))+(self.TRIBE_WINS-self.TRIBE_LOSE)


    if __name__ == "__main__":
        __init__()
