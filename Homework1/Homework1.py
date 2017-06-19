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
    def __init__(self, data, farmer=None, fox=None, goose=None, grain=None):
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
    
    farmer = np.copy
    
    
    

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



