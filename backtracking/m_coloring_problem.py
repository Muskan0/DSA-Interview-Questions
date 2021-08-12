# https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#

# Function to determine if graph can be coloured with at most M colors such
# that no two adjacent vertices of graph are coloured with same color.
def graphColoring(graph, M, V):
    color=[0]*V
    if solve(graph, M, V, 0, color):
        return True
    else:
        return False

def solve(graph, M , V, node, color):
    if node==V:
        return True
    # assign a color to the node
    # for every assigned color check if
    # configuration is safe.
    for i in range(1,M+1):
        if isSafe(graph, V, node, color, i):
            color[node]=i
            # recursively call the function for the next node
            if solve(graph, M, V, node+1, color):
                return True
            color[node]=0
    
    return False

# This function checks if we can safely
# assign the given color to the node.
# if any neigbhor of the node have the 
# same color, then return false
# otherwise this color can be assigned
# so return true.
# graph is based on adjacency matrix
def isSafe(graph, V, node, color, col):
    for i in range(V):
        if graph[node][i]==1:
            if color[i]==col:
                return False
    return True

# Time Complexity: O(M^V), because on every node, 
# we are trying to assign M colors.
# Space Complexity: O(N) for color array + O(N) for 
# auxiliary space of recursive stack.
