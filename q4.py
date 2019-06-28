"""
implement a function that finds the node in a binary search tree
containing the minimum value in the tree
"""

"""
Title: Binary Search Tree
Author: Hintea, D.
Date: 2019
Availability: http://moodle.coventry.ac.uk
*/
"""
import unittest
def test_int(self):
    self.assertEqual(11, 10, 12, 4, 5, 64,6,8,12)

class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
#this function finds the minimum value in the tree.
def tree_find_min(tree): 
    if tree.left != None: # checks if there are node in the left tree
        tree_find_min(tree.left) # if there is a left node in the tree, then the function will find the minimum node 
    else:
        print(tree.value) # print function prints out the minimum tree 

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)

  tree_find_min(t)

  unittest.main()


