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


from enemy import *
from player import *
from functions import *
import explore #not completed

player=Player()
enemy=Enemy()
enemy_turn=["sickness_enemy","enemy_train","enemy_wood","enemy_steel","enemy_spear","enemy_reproduction"]
order=["player"]

## commands list -- If i missed something or you added some functions,please
##                  fill this array.
commands=["train warrior","stats","fight","reproduction","explore","build wall","collect wood","make steel","make spear"]
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

>collect wood -> collect wood

>make spear -> make spear to train warriors.

>make steel -> if you have explore it,you can produce it.

""" %(name.upper())

while True:
	while order[0]=="player":
	
		wish=raw_input("Your command >>")
		if wish.lower()=="stats":
			print "TRIBE's MORAL="+player.TRIBE_MORAL
			print "TRIBE's POPULATION="+str(player.POP_TRIBE)
			print "----TRIBE'S RESOURCES----"
			print "food:%d" % player.TRIBE_RESOURCE["food"]
			print "wood:%d" % player.TRIBE_RESOURCE["wood"]
			print "steel:%d" % player.TRIBE_RESOURCE["steel"]
			print "spear:%d" % player.TRIBE_RESOURCE["spear"]

		elif wish.lower()=="reproduction":
			reproductionPlayer()
			order.append("opponent")
			order.remove("player")

		elif wish.lower()=="train warrior":
			number=input("How many warrior do you want to train?")
			if player.TRIBE_RESOURCE["food"]>=(number*5) and player.TRIBE_RESOURCE["spear"]>=(number*1) and player.TRIBE_RESOURCE["wood"]>=(number*10):
				player.TRIBE_RESOURCE["food"]-=5*number
				player.TRIBE_RESOURCE["spear"]-=1*number
				player.TRIBE_RESOURCE["wood"]-=10*number
				trainWarriorPlayer(number)
				order.append("opponent")
				order.remove("player")
			else:
				print "Your resources are not enough"
				print "You must have %d food,%d spear and %d wood at least to train %d warriors" %(((number*5)-player.TRIBE_RESOURCE["food"]),(number-player.TRIBE_RESOURCE["spear"]),((number*10)-player.TRIBE_RESOURCE["wood"]),number)

			
    
		elif wish.lower()=="build wall":
			buildWallPlayer()
			if player.TRIBE_WALLS==True:
				order.append("opponent")
				order.remove("player")
			
			
		elif wish.lower()=="fight":
			pass #for now
			
		elif wish.lower()=="collect wood":
			if player.POP_TRIBE>=2:
				collectWood()
			
		elif wish.lower()=="make steel":
			pass
		
		else:
			print("There is no such a command")
			
	while order[0]=="opponent":
		event=random.choice(enemy_turn)
		if event=="sickness_enemy":
			sickness_enemy()
			order.append("player")
			order.remove("opponent")
		elif event=="enemy_reproduction":
			reproductionEnemy()
			order.append("player")
			order.remove("opponent")
		elif event=="enemy_train":
			trainWarriorEnemy()
			if trainWarriorEnemy()==-1:
				continue
			else:
				order.append("player")
				order.remove("opponent")
