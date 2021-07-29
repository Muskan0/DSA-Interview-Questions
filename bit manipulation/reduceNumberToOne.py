'''
Problem: Given a number N, reduce it to 1, in minimum no of steps
by following the given operations:
1. If number is even, divide it by 2.
2. If it's odd, you can either increment or decrement it.

Approach 1:
Recursion but it has exponential time complexity.
def reduceto1(n):
  if n==1:
    return 0
  elif n%2==0:
    return 1+reduceto1(n//2)
  else:
    return 1+ min(reduceto1(n+1), reduceto1(n-1))
'''

# Approach 2

# Function for calculating min steps
# for reducing a number to 1
# Time complexity: O(log n)
def reduceto1(n):
    ans=0
    while n>1:
        # bitmask *0
        if n%2==0:
            n//=2
        # bitmask 01 or n is 3
        # n=3 is special edge case
        elif n%4==1 or n==3:
            n-=1
        # bitmask 11 
        # n%4==3 case
        else:
            n+=1
        ans+=1
    return ans

n=int(input())
print(reduceto1(n))
