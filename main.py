# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:11:15 2021

@author: amanullah.awan
"""
class Node(object):
    def __init__(self , val):
        self.left_child = None
        self.right_child = None
        self.val = val

class BinarySearchTree(object):
    def insert(self, root, node):
        if root is None:
            return node
        if root.val < node.val:
            root.right_child = self.insert(root.right_child , node)
        else:
            root.left_child = self.insert(root.left_child, node)
        return root
        
    def in_order(self , root):
        if not root:
            return None
        else:
            self.in_order(root.left_child)
            print (root.val)
            self.in_order(root.right_child)
        return root
    
    def pre_order(self, root):
        if not root:
            return None       
        else:
            print(root.val)
            self.pre_order(root.left_child)
            self.pre_order(root.right_child)
        return root
    
    def post_order(self , root):
        if not root:
            return None
        else:
            self.post_order(root.left_child)
            self.post_order(root.right_child)
            print (root.val)
        return root

#main()starts here
r = Node(3)
node = BinarySearchTree()
nodeList = [1, 8, 5, 12, 14, 6]

for nd in nodeList:
    node.insert(r, Node(nd))

print("--------In-Order-Travesal---------")
print(node.in_order(r))

print("--------Pre-Order-Travesal---------")
print(node.pre_order(r))

print("--------Post-Order-Travesal---------")
print(node.post_order(r))
    