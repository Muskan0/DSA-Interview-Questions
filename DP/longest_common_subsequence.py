# https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1#

def lcs(m,n,X,Y):
    '''
    :param m: length of string X 
    :param n: length of string Y
    :param X: string X
    :param Y: string Y
    :return: Integer
    '''
    
    t=[[-1 for i in range(n+1)] for j in range(m+1)]
    
    # initialization
    for i in range(0,m):
        for j in range(0,n):
            if i==0 or j==0:
                t[i][j]=0
                
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if X[i-1]==Y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j] , t[i][j-1])
    return t[m][n]
        
