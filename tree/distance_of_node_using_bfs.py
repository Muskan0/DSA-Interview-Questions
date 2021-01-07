# https://www.geeksforgeeks.org/distance-of-each-node-of-a-binary-tree-from-the-root-node-using-bfs/

class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

def findDistance(root, N):
    Q=[]
    Q.append(root)
    level=0
    dist=[0 for i in range(N+1)]
    while Q:
        M=len(Q)
        for i in range(0,M):
            root=Q[0]
            Q.pop(0)
            dist[root.data]=level
            if root.left:
                Q.append(root.left)
            if root.right:
                Q.append(root.right)
        level+=1
    for i in range(1,N+1):
        print(dist[i], end=" ")
if __name__=='__main__':
    N=7
    root=Node(5)
    root.left=Node(4)
    root.right=Node(6)
    root.left.left=Node(3)
    root.left.right=Node(7)
    root.left.left.left=Node(1)
    root.left.left.right=Node(2)
    findDistance(root,N)
