# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m/0#

for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    low=1
    high=m
    guess=(low+high)/2
    
    epsilon=0.0000001 # for taking approximations
    
    # binary search
    while abs(guess**n-m)>=epsilon:
        if guess**n>m:
            high=guess
        else:
            low=guess
        guess=(low+high)/2
    #print(round(guess))
    if m==round(guess)**n:
        print(int(round(guess)))
       # The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
       # The default number of decimals is 0, meaning that the function will return the nearest integer.
    else:
        print(-1)
