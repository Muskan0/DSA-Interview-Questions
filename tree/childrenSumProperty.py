'''
    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''
        
def changeTree(root): 
    if root is None:
        return
    
    temp=0
    if root.left:
        temp+=root.left.data
    if root.right:
        temp+=root.right.data
    if temp>=root.data:
        root.data=temp
    else:
        if root.left:
            root.left.data=root.data
        if root.right:
        	root.right.data=root.data
          
    changeTree(root.left)
    changeTree(root.right)
    
    temp=0
    if root.left:
        temp+=root.left.data
    if root.right:
        temp+=root.right.data
    if temp>root.data:
        root.data=temp
    return
  
# Time complexity: O(N), where N is no of nodes
# Space complexity: O(N), in case of skew tree
