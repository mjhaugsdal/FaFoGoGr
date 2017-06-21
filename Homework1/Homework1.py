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


goalReached = False
printCount = 0

import numpy as np
import sys
from pprint import pprint

class Tree:
    def __init__(self, data, parent = None, farmer=None, fox=None, goose=None, grain=None):
        parent = self
        self.data = data
        self.farmer = farmer
        self.fox = fox
        self.goose = goose
        self.grain = grain

    def _insertFarmer(self, newNode):
        if self.farmer == None:
            self.farmer = Tree(newNode)
        else:
            t = Tree(newNode)
            t.farmer = self.farmer
            self.farmer = t

    def _insertFox(self, newNode):
        if self.fox == None:
            self.fox = Tree(newNode)
        else:
            t = Tree(newNode)
            t.fox = self.fox
            self.fox = t

    def _insertGoose(self, newNode):
        if self.goose == None:
            self.goose = Tree(newNode)
        else:
            t = Tree(newNode)
            t.goose = self.goose
            self.goose = t

    def _insertGrain(self, newNode):
        if self.grain == None:
            self.grain = Tree(newNode)
        else:
            t = Tree(newNode)
            t.grain = self.grain
            self.grain = t

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

       # print(list
        #print(array
        if np.array_equal(list,array):
            return True
    #Else
    return False

def print_nicer(state):
    
    global printCount
    printCount+=1

    if printCount == 5:
        input("Press Enter to continue...")

    print("Move #", printCount)
 
    print()
    print("_________________________") 
    print("_________________________") 
    print()
    print("Left side:")
    print()
    print()

    if state[0] == 0:
        print("Farmer")
    if state[1] == 0:
        print("Fox")
    if state[2] == 0:
        print("Goose")
    if state[3] == 0:
        print("Grain")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~ ____ ~~~~~~~~~~~")
    print("~~~~~~~\    /~~~~~~~~~~~")
    print("~~~~~~~~\  /~~~~~~~~~~~~")
    print("~~~~~~~\_||__/~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Right side:")
    print()
    print()
    if state[0] == 1:
        print("Farmer")
    if state[1] == 1:
        print("Fox")
    if state[2] == 1:
        print("Goose")
    if state[3] == 1:
        print("Grain")    
    print()
    print()
    print("_________________________")  
    print("_________________________")      
    


def make_tree(x, par):
    
    #print (x.data)
    
    global goalReached
    
    
    if np.array_equal(x.data, [1,1,1,1]):
    #if x.data == [1,1,1,1]:
        goalReached = True
        print_nicer(x.data)
        print("Number of moves: ",printCount)

        
        
        
        return x
    elif goalReached == False:
        print_nicer(x.data)
        farmer = Tree(x.data[:])
        farmer.parent = x
    
        farmer.data[0] = flip_val(farmer.data[0])
        #Flips the farmer. The farmer can go across alone!
        if par != 1:
            if eval_state(farmer.data) == True:
        
                Tree._insertFarmer(x,farmer)
                #farmer.parent = farmer
         
        
                make_tree(farmer, 1)

        fox = Tree(farmer.data[:])
        fox.parent = x
        fox.data[1] = flip_val(fox.data[1])

        if par != 2:
    
            if x.data[0] == x.data[1]: #Only ferry if farmer is on same side
                if eval_state(fox.data) == True:

                    Tree._insertFox(x,fox)
             
                   
                    fox.parent = fox
                    make_tree(fox, 2)
             
        goose = Tree(farmer.data[:])
        goose.parent = x
        goose.data[2] = flip_val(goose.data[2])
    
        if par != 3:
            if x.data[0] == x.data[2]: #Only ferry if farmer is on same side
        
                if eval_state(goose.data) == True :

                        Tree._insertGoose(x,goose)
                       
                        goose.parent = goose
                        make_tree(goose, 3)    

        grain = Tree(farmer.data[:])
        grain.parent = x
        grain.data[3] = flip_val(grain.data[3])

        if par != 4:
            if x.data[0] == x.data[3]: #Only ferry if farmer is on same side
        
                if eval_state(grain.data) == True:

                        Tree._insertGrain(x,grain)
         
                        grain.parent = grain
                        make_tree(grain, 4)   
          

def create_root():

    x = Tree ([0,0,0,0])
    return x

def main():
    
    x = create_root()

    #while x.data != goal:
    x = make_tree(x, 0)
    
    #print (x.data)

    #print ("hello world")

main()



