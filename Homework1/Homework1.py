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
    def __init__(self, data, left=None, center=None, right=None):
        self.data = data
        self.left = left
        self.center = center
        self.right = right   

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

    legalStates = np.array([[0,0,0,0],
                           [1,0,1,0],
                           [0,0,1,0],
                           [1,1,1,0],
                           [0,1,0,0],
                           [1,0,1,1],
                           [0,0,0,1],
                           [1,1,0,1],
                           [0,1,0,1],
                           [1,1,1,1]])
    
    unsafeStates = np.array([[0,1,1,0],
                             [0,0,1,1],
                             [1,0,0,1],
                             [1,1,0,0],
                             [1,0,0,0],
                             [0,1,1,1]])


    #IF STATE IS IN LEGAL STATES
    for list in legalStates:

        print(list)
        print(array)

        if list.all == array:
            return True

    #Else
    return False
       # print (ret)

        #print (list)
        #compare(array)

   # return True
    #ELSE
    #return False



def create_root():

    x = Tree ([0,0,0,0])

    return x

def add_level(x):
    
    #Create boat, Flip farmer / put farmer on boat
    
    boat = Tree(x.data[:])
    boat.data[0] = flip_val(boat.data[0])

    #Create next level of nodes, with flipped values
    
    #Left
    left = Tree(boat.data[:])
    left.data[1] = flip_val(left.data[1])
   
    #Center
    center = Tree(boat.data[:])
    center.data[2] = flip_val(center.data[2])
    
    #Right
    right = Tree(boat.data[:])
    right.data[3] = flip_val(right.data[3])
    
    #Link level.
    ret = Tree(x.data,left,center,right)

    return ret


def main():

    #Starting node
    
    # x = Tree((0,0,0,0), Tree((1,0,1,0)), Tree((0,0,1,0)), Tree((1,1,1,0)))

    # Create a tree with root node
    x = create_root()

    print_tree(x)
    
    # While not done, add a level
    # 
    x = add_level(x)

    # Evaluate each child

    print (eval_state(x.data))

    print_tree(x)
    print_tree(x.left)
    print_tree(x.center)
    print_tree(x.right)

    print("Hello world")

    
    



main()



