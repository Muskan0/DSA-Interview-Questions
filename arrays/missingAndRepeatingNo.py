# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0
import math
for _ in range(int(input())):
    n=int(input())
    A=list(map(int, input().split()))
    '''
    # using equations
    s=n*(n+1)//2
    s2=n*(n+1)*(2*n+1)//6
    for i in A:
        s-=i
        s2-=(i*i)
    x=(s+(s2//s))//2
    y=x-s
    print(y,x,sep=" ")
 '''    
    # using bit manipulation
    xor=0
    global x,y
    x=0
    y=0
    for i in A:
        xor^=i
    for i in range(1,n+1):
        xor^=i
    
    #set_bit= 2**int(math.log(xor, 2)) 
    set_bit= xor & ~(xor-1)
    for i in A:
        if set_bit & i!=0:
            x^=i
        else:
            y^=i
    for j in range(1,n+1):
        if set_bit & j!=0:
            x^=j
        else:
            y^=j
    
    if x in A:
        print(x,y,sep=" ")
    else:
        print(y,x,sep=" ")
    
    
        
