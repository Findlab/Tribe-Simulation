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


#### FUNCTIONS by Mert ARIKAN - 2015 ####

import random
from player import *
from enemy import *
import explore

player=Player()
enemy=Enemy()

def loseWar():
    RESLIST=["food","spear","wood","steel"]
    player.TRIBE_LOSE+=5
    a=random.choice(RESLIST)
    b=random.randint(0,player.TRIBE_RESOURCE["%s"%(a)])
    if player.TRIBE_RESOURCE["%s"%(a)]!=0 and player.TRIBE_RESOURCE["%s"%a]>=b:
        player.TRIBE_RESOURCE["%s"%(a)]-=b
        enemy.ENEMY_RESOURCE["%s"%(a)]+=b
    elif player.TRIBE_RESOURCE["%s"%(a)]==0 and b>player.TRIBE_RESOURCE["%s"%a]:
        RESLIST.remove(a)
        while b>a:
            a=random.choice(RESLIST)
            if player.TRIBE_RESOURCE["%s"%a]>=b:
                player.TRIBE_RESOURCE["%s"%(a)]-=b
                enemy.ENEMY_RESOURCE["%s"%(a)]+=b
                break
    elif player.TRIBE_RESOURCE["%s"%(a)]!=0 and b>player.TRIBE_RESOURCE["%s"%a]:
        RESLIST.remove(a)
        while b>a:
            a=random.choice(RESLIST)
            if player.TRIBE_RESOURCE["%s"%a]>=b:
                player.TRIBE_RESOURCE["%s"%(a)]-=b
                enemy.ENEMY_RESOURCE["%s"%(a)]+=b
                break
        

        
def winWar():
    RESLIST=["food","spear","wood","steel"]
    player.TRIBE_WINS+=5
    a=random.choice(RESLIST)
    b=random.randint(0,enemy.ENEMY_RESOURCE["%s"%(a)])
    if enemy.ENEMY_RESOURCE["%s"%(a)]!=0 and enemy.ENEMY_RESOURCE["%s"%a]>=b:
        enemy.ENEMY_RESOURCE["%s"%(a)]-=b
        player.TRIBE_RESOURCE["%s"%(a)]+=b
    elif enemy.ENEMY_RESOURCE["%s"%(a)]==0 and b>enemy.ENEMY_RESOURCE["%s"%a]:
        RESLIST.remove(a)
        while b>a:
            a=random.choice(RESLIST)
            if enemy.ENEMY_RESOURCE["%s"%a]>=b:
                player.TRIBE_RESOURCE["%s"%(a)]+=b
                enemy.ENEMY_RESOURCE["%s"%(a)]-=b
                break
    elif enemy.ENEMY_RESOURCE["%s"%(a)]!=0 and b>enemy.ENEMY_RESOURCE["%s"%a]:
        RESLIST.remove(a)
        while b>a:
            a=random.choice(RESLIST)
            if enemy.ENEMY_RESOURCE["%s"%a]>=b:
                enemy.ENEMY_RESOURCE["%s"%(a)]-=b
                player.TRIBE_RESOURCE["%s"%(a)]+=b
                break
def explore_player():
    pass #for now




def explore_enemy():
    pass # for now.

def sickness_player(): # probability of sickness for player
    boo=["true","false"]
    if player.TRIBE_WINS-player.TRIBE_LOSE>=20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif player.TRIBE_WINS-player.TRIBE_LOSE>10 and player.TRIBE_WINS-player.TRIBE_LOSE<20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif player.TRIBE_WINS-player.TRIBE_LOSE<=10 and player.TRIBE_WINS-player.TRIBE_LOSE>5:
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif player.TRIBE_WINS-player.TRIBE_LOSE<=5 and player.TRIBE_WINS-player.TRIBE_LOSE>0:
        boo.append("false")
        boo.append("true")
    else:
        pass
    sec=random.choice(boo)
    if sec=="true":
        sick=random.randint(0,5)
        if player.POP_TRIBE>player.POP_TRIBE_SICK:
            if player.POP_TRIBE_SICK+sick<=player.POP_TRIBE:
                print "%d member(s) become sick now." % sick
                player.POP_TRIBE_SICK+=sick
            elif player.POP_TRIBE_SICK+sick>player.POP_TRIBE:
                player.POP_TRIBE_SICK=player.POP_TRIBE
                print("All members of tribe are sick!")
        elif player.POP_TRIBE_SICK==player.POP_TRIBE:
            print("All members of tribe are sick!")
        else:
            print("All members of tribe are sick!")
            player.POP_TRIBE_SICK=player.POP_TRIBE
        
    else:
        pass


def sickness_enemy(): # probability of sickness for enemy
    boo=["true","false"]
    if enemy.ENEMY_WINS-enemy.ENEMY_LOSE>=20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif enemy.ENEMY_WINS-enemy.ENEMY_LOSE>10 and enemy.ENEMY_WINS-enemy.ENEMY_LOSE<20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif enemy.ENEMY_WINS-enemy.ENEMY_LOSE<=10 and enemy.ENEMY_WINS-enemy.ENEMY_LOSE>5:
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif enemy.ENEMY_WINS-enemy.ENEMY_LOSE<=5 and enemy.ENEMY_WINS-enemy.ENEMY_LOSE>0:
        boo.append("false")
        boo.append("true")
    else:
        pass
    sec=random.choice(boo)
    if sec=="true":
        if enemy.POP_ENEMY_SICK<enemy.POP_ENEMY:
            sick=random.randint(0,5)
            if enemy.POP_ENEMY_SICK+sick<=enemy.POP_ENEMY:
                enemy.POP_ENEMY_SICK+=sick
            elif enemy.POP_ENEMY_SICK+sick>enemy.POP_ENEMY:
                enemy.POP_ENEMY_SICK=enemy.POP_ENEMY
        elif enemy.POP_ENEMY_SICK==enemy.POP_ENEMY:
            pass
        else:
            enemy.POP_ENEMY_SICK=enemy.POP_ENEMY
    else:
        pass


def reproductionPlayer():
    boo=["true","false"]
    if player.TRIBE_WINS-player.TRIBE_LOSE>=20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif player.TRIBE_WINS-player.TRIBE_LOSE>10 and player.TRIBE_WINS-player.TRIBE_LOSE<20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif player.TRIBE_WINS-player.TRIBE_LOSE<=10 and player.TRIBE_WINS-player.TRIBE_LOSE>5:
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif player.TRIBE_WINS-player.TRIBE_LOSE<=5 and player.TRIBE_WINS-player.TRIBE_LOSE>0:
        boo.append("false")
        boo.append("true")
    else:
        pass

    sec=random.choice(boo)
    if sec=="true":
        a=random.randint(0,10)
        player.POP_TRIBE+=a
        print "The number of your tribe's member increased %d" % (a)
    elif sec=="false":
        pass


def reproductionEnemy():
    boo=["true","false"]
    if enemy.ENEMY_WINS-enemy.ENEMY_LOSE>=20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif enemy.ENEMY_WINS-enemy.ENEMY_LOSE>10 and enemy.ENEMY_WINS-enemy.ENEMY_LOSE<20:
        boo.append("false")
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif enemy.ENEMY_WINS-enemy.ENEMY_LOSE<=10 and enemy.ENEMY_WINS-enemy.ENEMY_LOSE>5:
        boo.append("false")
        boo.append("false")
        boo.append("true")
    elif enemy.ENEMY_WINS-enemy.ENEMY_LOSE<=5 and enemy.ENEMY_WINS-enemy.ENEMY_LOSE>0:
        boo.append("false")
        boo.append("true")
    else:
        pass

    sec=random.choice(boo)
    if sec=="true":
        a=random.randint(0,10)
        enemy.POP_ENEMY+=a
    elif sec=="false":
        pass




def trainWarriorPlayer(number): #This function works if resources are avaible (Main Function)
    player.TRIBE_WARRIOR+=number
    

def trainWarriorEnemy():
    a=random.randint(0,10)
    if enemy.ENEMY_RESOURCE["food"]>=5 and enemy.ENEMY_RESOURCE["spear"]>=1 and enemy.ENEMY_RESOURCE["wood"]>=10 and enemy.ENEMY_WARRIOR+a<=enemy.POP_ENEMY:
        enemy.ENEMY_RESOURCE["food"]-=5
        enemy.ENEMY_RESOURCE["spear"]-=1
        enemy.ENEMY_RESOURCE["wood"]-=10
        enemy.ENEMY_WARRIOR+=a
    else:
        pass
    
def buildWallPlayer():
	if player.TRIBE_RESOURCE["wood"]>=120 and player.TRIBE_RESOURCE["steel"]>=50 and TRIBE_WALLS==False:
		player.TRIBE_WALLS=True
		print "Your wall has been built"
	elif TRIBE_WALLS==True:
		print "You have walls already"
	else:
		print "You don't have enough resource"
		print "wood %d/120 \n steel %d/50" %(player.TRIBE_RESOURCE["wood"],player.TRIBE_RESOURCE["steel"])
		

def enemyDecision():
    pass #to be continued...


