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

class Enemy:
    def __init__(self):
        self.POP_ENEMY=50 #The population of ENEMY
        self.ENEMY_RESOURCE={"food":random.randint(20,120),"spear":random.randint(0,self.POP_ENEMY),"wood":random.randint(50,200),"steel":0}
        self.ENEMY_WARRIOR=0
        self.ENEMY_WALLS=False
        self.ENEMY_MINER=0
        self.ENEMY_WOODMAN=0
        self.ENEMY_EXPLORER=0
        self.ENEMY_WINS=0 # ENEMY can gain win when they explore something,winning war...
        self.ENEMY_LOSE=0 #Losing war,the number of sick people...
        self.POP_ENEMY_SICK=0

        if self.ENEMY_WINS-self.ENEMY_LOSE>=20:
            self.ENEMY_MORAL="WONDERFUL!"
        elif self.ENEMY_WINS-self.ENEMY_LOSE>10 and self.ENEMY_WINS-self.ENEMY_LOSE<20:
            self.ENEMY_MORAL="VERY GOOD!"
        elif self.ENEMY_WINS-self.ENEMY_LOSE<=10 and self.ENEMY_WINS-self.ENEMY_LOSE>5:
            self.ENEMY_MORAL="GOOD!"
        elif self.ENEMY_WINS-self.ENEMY_LOSE<=5 and self.ENEMY_WINS-self.ENEMY_LOSE>0:
            self.ENEMY_MORAL="NOT BAD!"
        elif self.ENEMY_WINS-self.ENEMY_LOSE==0:
            self.ENEMY_MORAL="NEUTRAL"
        else:
            self.ENEMY_MORAL="BAD!!!"


        self.ENEMY_EXPLORE_CHANCE=self.ENEMY_EXPLORER*(2.13)+(self.ENEMY_WINS-self.ENEMY_LOSE)
        self.ENEMY_FIGHT_CHANCE=self.ENEMY_WARRIOR*(2.13)+(self.ENEMY_WINS-self.ENEMY_LOSE)
        if self.ENEMY_WALLS==True:
            self.ENEMY_DEFENCE_CHANCE=25+(self.ENEMY_WARRIOR*(3.14))+(self.ENEMY_WINS-self.ENEMY_LOSE)
        else:
            self.ENEMY_DEFENCE_CHANCE=5+(self.ENEMY_WARRIOR*(3.14))+(self.ENEMY_WINS-self.ENEMY_LOSE)



########################MAIN MODULE############################

#if ENEMY_RESOURCE["food"]>=5 and ENEMY_RESOURCE["spear"]>=1 and ENEMY_RESOURCE["wood"]>=10:
    #    ENEMY_RESOURCE["food"]-=5
     #   ENEMY_RESOURCE["spear"]-=1
      #  ENEMY_RESOURCE["wood"]-=10
   # else:
    #    print "Your resources are not enough"
     #   print "You must have 5 food,1 spear and 10 wood at least"
