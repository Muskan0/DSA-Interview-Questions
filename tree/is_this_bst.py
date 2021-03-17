# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

'''
The binary search tree is the tree with following properties:
1. The value of node in left subtree is less than value of it's parent node.
2. The value of node in right subtree is more than value of it's parent node.
---> This implies that each node in the tree is distinct.

Constraints:
0<=data<=10^4
'''

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def bst(root, x, y):
    if root==None:
        return True
    if root.data<= x or root.data>= y:
        return False
    return bst(root.left, x,root.data) and bst(root.right, root.data, y )
    
        
    
def check_binary_search_tree_(root):
    return bst(root,-1,99999)
  
  '''
  Time complexity: O(N)
  Space Complexity: O(N), for function call stack
  '''
