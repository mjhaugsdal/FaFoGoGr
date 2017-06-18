#!/usr/bin/python
# CSC 547 Artificial Intelligence
# Lecturer: Sung Shin
# 
# Date: 6/17/2017
# Author: Markus Haugsdal
#
# Resources used: https://www.tutorialspoint.com/python/index.htm
#                 http://openbookproject.net/thinkcs/python/english3e/trees.html
#
# Homework 2 
# Due date: 6-21
#

import numpy as np
import sys
from enum import Enum

class Tree:
    def __init__(self, data, grandpa=None, isValid=True , farmer=None, fox=None, goose=None, grain=None):
        self.grandpa = grandpa
        self.data = data
        self.isValid = isValid
        self.farmer = farmer
        self.fox = fox
        self.goose = goose
        self.grain = grain   

    def __str__(self):
        return str(self.data) 

def print_tree(tree):
    #print(tree)
    print(tree.data)

def flip_val(val):
   
    if val == 1:
        val = 0
    else:
        val = 1
    return val


def cmp(a, b):
    return (a > b) - (a < b) 

def eval_state(array):

    array = np.asarray(array) 
    legalStates = np.array([[0 ,0 ,0 ,0],
                           [1,0,1,0],
                           [0,0,1,0],
                           [1,1,1,0],
                           [0,1,0,0],
                           [1,0,1,1],
                           [0,0,0,1],
                           [1,1,0,1],
                           [0,1,0,1],
                           [1,1,1,1]])
    
   # unsafeStates = np.array([[0,1,1,0],
   #                          [0,0,1,1],
   #                          [1,0,0,1],
   #                          [1,1,0,0],
   #                          [1,0,0,0],
   #                          [0,1,1,1]])


    #IF STATE IS IN LEGAL STATES
    for list in legalStates:

       # print(list)
        
        
        #print(array)


        if np.array_equal(list,array):
            return True
       # if np.all(list) == np.all(array):
       #     print ("True")
       #     return True

    #Else
    #print("Returned false")
    return False

def create_root():

    x = Tree ([0,0,0,0])

    return x




def go_left(x):
    
    #Create boat, Flip farmer / put farmer on boat
    
    #Farmer
    boat = Tree(x.data[:])
    
    if boat.data[0] == 0:    
        boat.data[0] = flip_val(boat.data[0])

    if eval_state(boat.data) == False:
        boat.isValid = False
        
    #print(boat.data)
    #Create next level of nodes, with flipped values
    
    #Fox
    Fox = Tree(boat.data[:])
    if Fox.data[0] == 0:    
        Fox.data[1] = flip_val(Fox.data[1])

    if eval_state(Fox.data) == False:
        Fox.isValid = False
   
    #Goose
    Goose = Tree(boat.data[:])
    if Goose.data[0] == 0:    
        Goose.data[2] = flip_val(Goose.data[2])

    if eval_state(Goose.data) == False:
        Goose.isValid = False
    
    #Grain
    Grain = Tree(boat.data[:])
    if Grain.data[0] == 0:    
        Grain.data[3] = flip_val(Grain.data[3])

    if eval_state(Grain.data) == False:
        Grain.isValid = False    


    #Link level. #boat == farmer
    ret = Tree(x.data, boat, Fox, Goose, Grain)

    return ret


def go_right(x):

    #Create boat, Flip farmer / put farmer on boat
    
    #Farmer
    boat = Tree(x.data[:])
    
    if boat.data[0] == 0:    
        boat.data[0] = flip_val(boat.data[0])

    if eval_state(boat.data) == False:
        boat.isValid = False
        
    #print(boat.data)
    #Create next level of nodes, with flipped values
    
    #Fox
    Fox = Tree(boat.data[:])
    if Fox.data[0] == 0:    
        Fox.data[1] = flip_val(Fox.data[1])

    if eval_state(Fox.data) == False:
        Fox.isValid = False
   
    #Goose
    Goose = Tree(boat.data[:])
    if Goose.data[0] == 0:    
        Goose.data[2] = flip_val(Goose.data[2])

    if eval_state(Goose.data) == False:
        Goose.isValid = False
    
    #Grain
    Grain = Tree(boat.data[:])
    if Grain.data[0] == 0:    
        Grain.data[3] = flip_val(Grain.data[3])

    if eval_state(Grain.data) == False:
        Grain.isValid = False    


    #Link level. #boat == farmer
    ret = Tree(x.data, boat, Fox, Goose, Grain)

    return ret
    


def addNode(x):

        print("It")
        print (x)
        # Evaluate each child
        # Recursively go through all children

        #Farmer
        if (x.farmer):
            if x.farmer.isValid == True:
                
         
                x.farmer = add_level(x.farmer)
                
                x.farmer = addNode(x.farmer)
        #Fox
        if(x.fox):
            if x.fox.isValid == True:
               
                x.fox = add_level(x.fox)
                x.fox = addNode(x.fox)

       # print (eval_state(x.data))
       # print_tree(x.fox)
    
        #print (x.fox)
        if(x.goose):
            if x.goose.isValid == True:
               
                x.goose = add_level(x.goose)
                x.goose = addNode(x.goose)
       
        #print (eval_state(x.data))
        #print_tree(x.goose)

        if(x.grain):
            if x.grain.isValid == True:
                x.grain = add_level(x.grain)
                x = addNode(x.grain)

        #print (eval_state(x.data))
        #print_tree(x.grain)

def main():

    
    #Goal node
    goal = [1,1,1,1]
    #Starting node
    
    # x = Tree((0,0,0,0), Tree((1,0,1,0)), Tree((0,0,1,0)), Tree((1,1,1,0)))

    # Create a tree with root node
    x = create_root()

    # While not done, add a level
    # 
    x = add_level(x)
    #print(x)
    print(x.farmer.isValid)

    #while x.data != goal:
        #print(x)
    print ("hello")
    add_level(x, 1)

main()



