# FaFoGoGr

Farmer - Fox - Goose - Grain - problem

So, whats going on here? First, the program is given the rules of the problem, see https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem.

Then, using an array of legal states it creates a tree using current state as root, choosing only legal moves. 
It does not choose randomly, but creates new nodes using current state and a pointer to its parent.
