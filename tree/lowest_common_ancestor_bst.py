# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1#
'''
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 
is defined as the lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).
'''

'''
# recursive approach
def LCA(root, n1, n2):
    if root:
        if root.data>n1 and root.data>n2:
            return LCA(root.left, n1, n2)
        elif root.data<n1 and root.data<n2:
            return LCA(root.right, n1, n2)
        
    return root
'''

# iterative approach
# Returns the LCA of the nodes with values n1 and n2
# in the BST rooted at 'root' 
def LCA(root, n1, n2):
    while root:
        # LCA lies in left subtree
        if root.data>n1 and root.data>n2:
            root=root.left
        # LCA lies in right subtree
        elif root.data<n1 and root.data<n2:
            root=root.right
        # current node is LCA
        else:
            break
    return root
