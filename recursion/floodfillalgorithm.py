# https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0

# solved using recursion

import numpy as np
def floodfill(mg,x,y,prevColor,color):
    if(x<0 or y<0 or x>=n or y>=m or mg[x][y]!=prevColor):
        return
    mg[x][y]=color
    floodfill(mg,x+1,y,prevColor,color)
    floodfill(mg,x-1,y,prevColor,color)
    floodfill(mg,x,y+1,prevColor,color)
    floodfill(mg,x,y-1,prevColor,color)
for _ in range(int(input())):
    n,m=map(int, input().split())
    l=list(map(int, input().split()))
    mg=np.reshape(l,(n,m))
    x,y,color=map(int, input().split())
    prevColor=mg[x][y]
    floodfill(mg,x,y,prevColor,color)
    l=np.reshape(mg,-1)
    for i in l:
        print(i, end=" ")
    print()
