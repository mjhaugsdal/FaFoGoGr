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

class Tree:
    def __init__(self, data, parent = None, farmer=None, fox=None, goose=None, grain=None):
        self.parent = self
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


def make_tree(x):
    
   # x.parent = x.data
    
    #x.parent = x.data #Save the parent
    farmer = Tree(x.data[:])
    print("Parent")
    print(x.parent.parent.data)
    
    
    farmer.data[0] = flip_val(farmer.data[0])
    #Flips the farmer. The farmer can go across alone!

    if eval_state(farmer.data) == True:

        print("Here")
        print(farmer.parent.parent.data)
        print(farmer.data)

        Tree._insertFarmer(x,farmer)
        #farmer.parent = farmer
        print("Inserted Farmer")
        
        
        make_tree(farmer)

    fox = Tree(farmer.data[:])
    fox.data[1] = flip_val(fox.data[1])

    if x.data[0] == x.data[1]: #Only ferry if farmer is on same side
        if eval_state(fox.data) == True:
             
            Tree._insertFox(x,fox)
            print("Inserted Fox")
            print(fox.data)
            fox.parent = fox
            make_tree(fox)
    
    goose = Tree(farmer.data[:])
    goose.data[2] = flip_val(goose.data[2])
    

        


    if x.data[0] == x.data[2]: #Only ferry if farmer is on same side
        
        if eval_state(goose.data) == True :
            
            Tree._insertGoose(x,goose)
            print("Inserted Goose")
            print(goose.data)
            goose.parent = goose
            make_tree(goose)
        
    grain = Tree(farmer.data[:])
    grain.data[3] = flip_val(grain.data[3])

    if x.data[0] == x.data[3]: #Only ferry if farmer is on same side
        
        if eval_state(grain.data) == True:
            
            Tree._insertGrain(x,grain)
            print("Inserted grain")
            print(grain.data)
            grain.parent = grain
            make_tree(grain)
 
def create_root():

    x = Tree ([0,0,0,0])
    return x

def main():
    
    x = create_root()
    goal = [1,1,1,1]

    #while x.data != goal:
    make_tree(x)
            
    


    
    print ("hello world")

main()



